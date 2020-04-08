# example Flask Server
# to run, in cli within pipenv shell virtual env: python hello.py

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"

if __name__ == "__main__":
    app.run()