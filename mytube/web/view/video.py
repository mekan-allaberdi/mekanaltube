import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

import json
import logging

from flask import Blueprint, request, render_template, redirect, url_for, session, abort
bp = Blueprint('root', __name__)

from mytube.web.access import video_access


@bp.route('/', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        validation_errors = []
        name_text = request.form.get('name', '').strip()
        theme_text = request.form.get('theme', '').strip()
        if not name_text or not theme_text:
            validation_errors.append('Please fill all fields')
        if len(validation_errors) > 0:
            return render_template('video.html', val_errors=validation_errors)
        else:
            video_access.create(name=name_text, theme=theme_text.lower())

    video_list = video_access.get_all()
    return render_template('video.html', items=video_list)


@bp.route('/upvote/<string:id>', methods=['POST'])
def upvote(id):
    video_access.upvote(id)
    return redirect(url_for('root.add'))


@bp.route('/downvote/<string:id>', methods=['POST'])
def downvote(id):
    video_access.downvote(id)
    return redirect(url_for('root.add'))