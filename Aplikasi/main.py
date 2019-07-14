import flask
from flask import Flask, request, render_template, flash
from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.validators import Required
from wtforms.fields import html5

import matplotlib.pyplot as plt  
import numpy as np  
from sklearn.cluster import KMeans
import pandas

app = Flask(__name__)
app.secret_key = '7d441f27d441f27567d441f2b6176a'

class InputForm(FlaskForm):
    marmer = TextField(validators=[Required()])
    semen = TextField(validators=[Required()])
    kayu = TextField(validators=[Required()])
    lain = TextField(validators=[Required()])
    jambansendiri = TextField(validators=[Required()])
    jambanbersama = TextField(validators=[Required()])
    w450 = TextField(validators=[Required()])
    w900 = TextField(validators=[Required()])
    w1300 = TextField(validators=[Required()])
    w2200 = TextField(validators=[Required()])

    @app.route('/', methods=['POST'])
    def send():
        form = InputForm(request.form)
        if form.validate():
           print('Validation Success')
        else:
            print('Validation error')

        #perhitungan prediksi
        flname = "dataset.csv"
        data_train = pandas.read_csv(flname)
        data_train = data_train[['marmer','semen','kayu','lainnya','jambansendiri','jambanbersama','450w','900w','1300w','2200w']]
        X = data_train.values
        kmeans = KMeans(n_clusters=2)  
        kmeans.fit(X)
        kmeans.cluster_centers_
        kmeans.labels_
        inpt = [form.marmer.data,form.kayu.data,form.semen.data,form.lain.data,form.jambansendiri.data,form.jambanbersama.data,form.w450.data,form.w900.data,form.w1300.data,form.w2200.data]
        result = kmeans.predict([inpt]) 
        print(result)
        flash(str(result))

        return render_template('public.html', form=form)

    @app.route('/')
    def index():
        form = InputForm()
        return render_template('public.html', form=form)

if __name__ == "__main__":
    app.debug = True
    app.run()
