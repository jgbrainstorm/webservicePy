from flask import Flask, request, render_template
import json
import pylab as pl
import numpy as np
from pattern.en import sentiment
app = Flask(__name__)


@app.route('/',methods=["GET","PUT","POST"])
#@app.route('/')

def index():
    #data = json.loads(request.data)
    #data = request.data # if send in a json string, use request.data.
    comment = request.form['comment'] # if send in from a html form, use request.form
    usrname = request.form['usrname']
    senti = sentiment(comment)[0]
    #msg = data.get('message')
    #msg = 'test'
    return render_template('web_interface.html', comment=comment.strip(), usrname=usrname.strip(),sentiment=senti)


if __name__ == '__main__':
    app.run(debug=True)


