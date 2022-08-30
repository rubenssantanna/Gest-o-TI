# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y4VQZ-3nf-E9X6GN-a_bwFzyGGIf8B-A
"""

from crypt import methods
from webbrowser import get
from flask import Flask, render_template, request
import numpy as np
import pickle
app=Flask(__name__)
model=pickle.load(open('classificação Binaria Saude.pkl', 'rb'))
@app.route('/', methods= ["GET"])
def Home():
    return render_template('index.html')
@app.route("/predict", methods= ["POST"])
def predict():
    if request.method== "POST":
        BMI=int(request.form['BMI'] )
        values= np.array( ["BMI"])
        prediction= model.predict(values)
        return render_template('result.html', predictions= predictions)
   
if __name__== '_main_':
    app.run(debug=True)