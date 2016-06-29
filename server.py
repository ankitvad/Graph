# This is the code for editing the graph database using GUI mode

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to Graph Editor"

if __name__ == "__main__":
    app.run()