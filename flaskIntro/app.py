from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# __name__ references cur file
app = Flask(__name__ )
# telling the app where the db is located
# /// is relative, //// is absolute
# test.db is storing the data
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

#init db with settings from the app
db = SQLAlchemy(app)

#make a db model
class Todo(db.Model):
	#colum & column types
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(200), nullable=False)
	date_created = db.Column(db.DateTime, default=datetime.utcnow)

	#returns taskID
	def __repr__(self):
		return '<Task %r>' % self.id
 
# index route
# accepts 2 methods, declared in the methods arr
@app.route('/', methods=['POST', 'GET'])
def index():
	#return "Hello, world!"

	#POST handler
	if request.method == "POST":

		task_content = request.form['content']
		new_task = Todo(content=task_content)

		#try adding task to db && redirecting to root page
		try:
			db.session.add(new_task)
			db.session.commit()
			return redirect('/')
		except:
			return 'there was an issue adding your task'

	#Return the index page on GET
	else:
		#get all tasks from db
		tasks = Todo.query.order_by(Todo.date_created).all()

		#Here, flask "knows" to look in the 'templates' dir
		#"tasks" is param-name passed to the index.html template
		return render_template('index.html', tasks=tasks)


# DELETE To-Do item
@app.route('/delete/<int:id>')
def delete(id):
	task_to_delete = Todo.query.get_or_404(id)

	try:
		db.session.delete(task_to_delete)
		db.session.commit()
		return redirect('/')
	except: return 'There was a problem deleting that task'

@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):

	#get task from db
	task = Todo.query.get_or_404(id)

	if request.method == 'POST':
		pass
	else:
		return render_template('update.html', task=task)


if __name__ == "__main__":
	app.run(debug=True)