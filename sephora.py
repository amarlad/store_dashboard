# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 05:51:38 2019

@author: amar.lad
"""

import json
import os
import logging
from flask import Flask, render_template


BASEDIR = "C:\SephoraApp\static\json" 
jsonFilename = 'JASON_store_latitude_longitude.json'

def readJSON(jsonBASEDIR, jsonFilename):
    reader = None
    try:
        jsonFile = open(os.path.join(jsonBASEDIR, jsonFilename))
        reader = json.load(jsonFile)
    except IOError:
        logging.exception('')
    if not reader:
        raise ValueError('No data available')
    return reader

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])

def index():
    jsonReader = readJSON(BASEDIR, jsonFilename)
    return render_template("index.html", jsonReader=jsonReader)