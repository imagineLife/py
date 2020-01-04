from flask import Flask, render_template

# __name__ references cur file
app = Flask(__name__ )

# index route
@app.route('/')
def index():
	#return "Hello, world!"

	#Here, flask "knows" to look in the 'templates' dir
	return render_template('index.html')

if __name__ == "__main__":
	app.run(debug=True)