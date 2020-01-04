from flask import Flask

# __name__ references cur file
app = Flask(__name__ )

# index route
@app.route('/')
def index():
	return "Hello, world!"

if __name__ == "__main__":
	app.run(debug=True)