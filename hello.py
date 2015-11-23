from flask import Flask
from flask import request
import json
import pylab as pl
import numpy as np
app = Flask(__name__)


#@app.route('/',methods=["GET","PUT","POST"])
@app.route('/')
def index():
    #data = json.loads(request.data)
    #msg = data.get('message')
    msg = 'test'
    return msg


if __name__ == '__main__':
    app.run(debug=True)


