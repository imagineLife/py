from flask import Flask, render_template
from flask_sqlalchemy import sqlAlchemy
# __name__ references cur file
app = Flask(__name__ )
# telling the app where the db is located
# /// is relative, //// is absolute
# test.db is storing the data
app.config['SQLALCEMY_DATABASE_URI'] = 'sqlite:///test.db'

#init db with settings from the app
db = sqlAlchemy(app)

# index route
@app.route('/')
def index():
	#return "Hello, world!"

	#Here, flask "knows" to look in the 'templates' dir
	return render_template('index.html')

if __name__ == "__main__":
	app.run(debug=True)