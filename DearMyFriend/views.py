
from flask import render_template, request, url_for, redirect, flash
from flask_login import login_user, login_required, logout_user, current_user
from DearMyFriend import app,db
from DearMyFriend.models import User,Word

@app.route('/',methods=['GET','POST'])    
@app.route('/index',methods=['GET','POST'])
def show():
    if request.method=='POST':
        title=request.form['title']
        text=request.form['text']
        author=1
        word=Word(title=title,text=text,author=author)
        db.session.add(word)
        db.session.commit()   
        return render_template('index.html',comments=Word.query.order_by(Word.id.desc()).all())
    return render_template('index.html',comments=Word.query.order_by(Word.id.desc()).all())