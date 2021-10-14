
from flask import render_template, request, url_for, redirect, flash
from flask_login import login_user, login_required, logout_user, current_user
from DearMyFriend import app,db
@app.route('/',methods=['GET','POST'])    
@app.route('/index',methods=['GET','POST'])
def show():
    if request.method=='POST':
        
        return render_template('index.html',method='POST')
    return render_template('index.html',method='GET')