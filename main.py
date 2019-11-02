# coding: utf-8

import os
from bottle import Bottle, TEMPLATE_PATH, template, static_file

app = Bottle()
TEMPLATE_PATH.append("./templates")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.get("/css/<filename:path>")
def send_static(filename):
    # return static file path
    return static_file(filename, root=f'{BASE_DIR}/res/css/')

@app.route("/")
def default():
    return template("default.html", msg="Hello world")


if __name__ == '__main__':
    app.run(host='localhost', port=8080, reloader=True, debug=True)
