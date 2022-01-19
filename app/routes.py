import re
from flask import render_template
from app import app
from app.forms import RegisterForm

@app.route('/')

def nav():
    return render_template('nav.html')

     
def info():
    my_name="Gerardo"
    my_phone="(321)321-2314"
    my_address='342 Nice St, Detroit,MI 32134'
    return render_template('index.html',name=my_name,phone=my_phone,address=my_address)

def index():
    form = RegisterForm()
    if form.validate_on_submit():
        print('FORM HAS BEEN VALIDATED!')
        full_name= form.full_name.data
        phone_number= form.phone_number.data
        address=form.address.data
        return ('index.html')


    return render_template('index.html', form = form)