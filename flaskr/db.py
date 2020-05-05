import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    # g is a special object that is unique for each request.
    # It is used to store data that might be accessed by multiple functions during the request.
    if 'db' not in g:
        # current_app is another special object that points to the Flask application handling the request.
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    # tells Flask to call the passed-in function when cleaning up after returning the response
    app.teardown_appcontext(close_db)
    # add a new command that can be called with the flask command
    app.cli.add_command(init_db_command)
