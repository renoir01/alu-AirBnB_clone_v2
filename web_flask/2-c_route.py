#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display Hello HBNB!
/hbnb: display HBNB
You must use the option strict_slashes=False in your route definition
"""


from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def root_display():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_display():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_display(text):
    text_str = " ".join(text.split("_"))
    return "C {0}".format(text_str)

if __name__ == "__main__":
    # specify IP address and port number
    app.run(host="0.0.0.0", port=5000)
