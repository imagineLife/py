from flask import Flask, render_template, request
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
		return 'Hello submitted!'

	#Return the page on GET
	else:
		#Here, flask "knows" to look in the 'templates' dir
		return render_template('index.html')

if __name__ == "__main__":
	app.run(debug=True)