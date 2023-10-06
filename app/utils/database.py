import sqlite3

import psycopg2
from flask import Flask, abort, current_app, g

from app.utils.response import error_response, success_response


def get_db():
    """
    Returns a database connection from the application context.
    If there is no connection, it creates a new one and stores it in the application context.
    """
    if "db" not in g:
        # g.db = sqlite3.connect(current_app.config.get("SQLALCHEMY_DATABASE_URI"))
        # g.db.row_factory = sqlite3.Row

        try:
            g.db = psycopg2.connect(current_app.config.get("SQLALCHEMY_DATABASE_URI"))
        except psycopg2.OperationalError as e:
            return abort(500)

    return g.db


def close_db(e=None):
    """
    Closes the database connection if it exists.
    """
    db = g.pop("db", None)

    if db is not None:
        db.close()
