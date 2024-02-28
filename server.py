from flask import Flask
from flask import request
app = Flask (__name__)
@app.route ('/')
def hello_world ():
    return "Hello World"

@app.route ('/dojo')
def print_dojo ():
    return "Dojo!"

@app.route ('/say/<string:name>')
def print_say (name):
        return f"Hi {name}"

@app.route ('/<int:num>/<string:word>')
def repeat (word, num):
    return f"{word * num}"

@app.route('/<path:path>')
def handle_not_found (path):
    return "This route is not specified in the application" 

if __name__ == "__main__":
    app.run(debug = True, host = "localhost", port = 8000)
