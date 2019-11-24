#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 14:40:52 2019

@author: javiercarmona
"""

from flask import Flask
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    titulo = "GeekyFlask"
    usuario = {'nombre': 'Alejandro'}
    return render_template('index.html',
                           titulo=titulo,
                           usuario=usuario)#render_template('index.html')

if __name__ == "__main__":
    app.run()