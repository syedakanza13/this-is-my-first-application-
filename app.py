from flask import Flask

# Initialize the Flask application
app = Flask(__name__)


# Define the route for the homepage
@app.route("/")
def home():
    return "<h1>Hello, Flask!</h1>"
