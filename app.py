#!/usr/bin/env python
from flask import Flask, render_template, redirect
import pumpkin


app = Flask(__name__)

#Home page
@app.route('/')
def index():
    return render_template('index.html')


#Page 2
@app.route('/page2')
def cakes():
    return 'Page 2'


#Dynamic example page
@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)


#Run 'laugh1' script
@app.route('/laugh1')
def laugh1():
    pumpkin.laugh1()
    return redirect('/')


#Run 'laugh3' script
@app.route('/laugh3')
def laugh3():
    pumpkin.laugh3()
    return redirect('/')


#Run 'scream1' script
@app.route('/scream1')
def scream1():
    pumpkin.scream1()
    return redirect('/')


#Run 'monster1' script
@app.route('/monster1')
def monster1():
    pumpkin.monster1()
    return redirect('/')


#Run 'TRex1' script
@app.route('/TRex1')
def TRex1():
    pumpkin.TRex1()
    return redirect('/')


#Start server: 127.0.0.1:5000
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
