from flask import render_template
from multiprocessing import Value

from app import app

counter = Value('i', 0)

@app.route('/')
def index():
  with counter.get_lock():
    counter.value += 1
    out = counter.value
  return render_template("index.html", count=out)



