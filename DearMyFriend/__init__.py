import os
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

WIN=sys.platform.startswith("win")
if WIN:
    DbPrefix="sqlite:///"
else:
    DbPrefix="sqlite:////"

app=Flask(__name__)
app.config['SECRET_KEY']=os.getenv('SECRET_KEY','dev')
app.config['SQLALCHEMY_DATABASE_URI'] = DbPrefix+os.path.join(os.path.dirname(app.root_path),os.getenv('DATABASE_FILE','data.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

login_manager=LoginManager(app)

@login_manager.user_loader

def load_user(id):
    from DearMyFriend.models import User
    return User.query.get(int(id))

login_manager.login_view = 'login'

#@app.context_processor
#def now_uesr():
    #from DearMyFriend.models import User
    #user=User.query.       


 
from DearMyFriend import error,cmd,views
