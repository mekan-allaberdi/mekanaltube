#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import configparser
import logging.config
import decimal
import json
import os

from flask import Flask, request, Markup, render_template, session, jsonify
from flask_pymongo import PyMongo


app = None
mail = None
log = logging.getLogger(__name__)


def configure(db_uri, secret_key):
    app = Flask(__name__)


    app.secret_key = secret_key
    from mytube.web.access import db
    app.db = db

    from view.video import bp as video_bp
    from view.theme import bp as theme_bp

    app.register_blueprint(video_bp, url_prefix='')
    app.register_blueprint(theme_bp, url_prefix='/theme')

    @app.errorhandler(405)
    def method_not_allowed(error):
        message = {
            'message': error.description,
        }
        resp = jsonify(message)
        resp.status_code = 405
        return resp

    @app.errorhandler(404)
    def page_not_found(error):
        message = {
            'message': error.description,
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp

    @app.errorhandler(403)
    def page_forbidden(error):
        message = {
            'message': error.description,
        }
        resp = jsonify(message)
        resp.status_code = 403
        return resp

    return app


def run_web():
    db_uri = "mongodb://localhost:27017/mytubedb"
    local_app = configure(db_uri=db_uri,
                          secret_key=b'\xca\tC\x16\xca\xf5\xcb\x87\xb9I\x93[\xdd[C\xff^\x00k@Tg\xce\xef')
    local_app.jinja_env.auto_reload = True
    local_app.run(host='0.0.0.0', port='1818', debug=True)


def configure_uwsgi_app():
    config_file = 'config.ini'
    logging.config.fileConfig(config_file)
    config = configparser.ConfigParser()
    config.read(config_file)
    db_uri = config['mytube']['db_uri']
    engine = create_engine(db_uri,
                           convert_unicode=True)
    db_session = scoped_session(sessionmaker(autocommit=False,
                                             autoflush=False,
                                             bind=engine))

    local_app = configure(db_uri=db_uri,
                          db_session=db_session,
                          secret_key=os.urandom(24))
    return local_app


if __name__ == '__main__':
    run_web()

