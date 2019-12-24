from flask import Flask, render_template
import pandas as pd
import numpy as np 


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello API test with Flask'


@app.route('/testanalysis')
def hello_world2():
    return 'Second Test Page'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')