import click

import click
from DearMyFriend import db,app

@app.cli.command()
def init():
    db.drop_all()
    db.create_all()
    click.echo("创建数据库完成")