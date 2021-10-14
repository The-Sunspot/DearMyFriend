import string
import click
import random
from DearMyFriend import db,app
from DearMyFriend.models import User,Word

@app.cli.command()
def initdb():
    """Initialize the database."""
    db.drop_all()
    db.create_all()
    click.echo("创建数据库完成")

@app.cli.command()
@click.option('--username', prompt=True, help='The username used to login.')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='The password used to login.')
def admin(username,password):
    '''管理员'''
    db.create_all()
    user=User.query.filter(User.name==username).first()
    
    if user is not None:
        click.echo('更新用户')
        user.username = username
        user.set_password(password)
    else:
        click.echo('创建用户')
        user = User(name=username)
        user.set_password(password)
        db.session.add(user)
    click.echo(user.name)
    db.session.commit()
    click.echo('成功')

@app.cli.command()
def delWord():
    """清除Word库"""
    while Word.query.count()>0:
        db.session.delete(Word.query.first())
    db.session.commit()
    click.echo("Word库清空")

@app.cli.command()
def initdata():
    '''填充1000个初始数据'''
    for i in range(1,1001):
        author=1
        title=ranstr(10)
        text=ranstr(20)
        db.session.add(Word(title=title,author=author,text=text))
    db.session.commit()
    click.echo("填充了1000个数据")

def ranstr(num):
    return ''.join(random.sample(string.ascii_letters + string.digits, num))
     