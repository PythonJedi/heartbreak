#! /usr/bin/python

# Python flask server for the IEEE hearbreak hackathon
# Author: Tim Hewitt
# Date: 2016-02-13

from flask import Flask, request
from flask.ext.cors import CORS
import driver
print "Returned to flask"
app = Flask(__name__)
CORS(app)


@app.route("/")
def ping():
    print "ping!"
    return ""

@app.route("/up")
def up():
    print "up!"
    driver.up(range=220)
    return ""

@app.route("/down")
def down():
    print "down!"
    driver.down(range=170)
    return ""
    
@app.route("/lock")
def lock():
    print "lock!"
    driver.lock()
    return ""

@app.route("/fire")
def fire():
    print "fire!"
    driver.fire()
    return ""

        
if __name__ == "__main__":
    app.run(host='127.0.0.1', port= '6161', debug=False)
    driver.kill_connection()
