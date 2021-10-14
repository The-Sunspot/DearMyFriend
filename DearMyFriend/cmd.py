
import click
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
