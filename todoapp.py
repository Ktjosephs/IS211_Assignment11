#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Week 11 Assignment."""

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import re

app = Flask(__name__)

todo = []

class Task:

    def __init__(self, task, owner, priority):
        self.task = task
        self.owner = owner
        self.priority = priority


@app.route('/')
def display():

    return render_template('display.html', todo=todo)


@app.route('/submit', methods=['POST'])
def submit():

    global status
    task = request.form['task']
    owner = request.form['email']
    priority = request.form['priority']

    if task == "":
        status = "Error: A task is required."
        return redirect("/")
    elif not re.search(r"[^@]+@[^@]+\.[^@]+", owner):
        status = "Error: Invalid Email."
        return redirect("/")
    elif priority != "High" and priority != "Medium" and priority != "Low":
        status = "Error: A priority level is required."
        return redirect("/")
    else:
        todo.append((task, owner, priority))

    return redirect("/")


@app.route('/clear', methods=['POST'])
def clear():

    del todo[:]
    return redirect("/")


@app.route('/delete', methods=['POST'])
def delete():

    delete_index = int(request.form['index'])
    del todo[delete_index]
    return redirect("/")

if __name__ == "__main__":
    app.run()
