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
