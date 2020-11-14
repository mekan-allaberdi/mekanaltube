import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

import json
import logging

from flask import Blueprint, request, render_template, redirect, url_for, session, abort
bp = Blueprint('theme', __name__)

from mytube.web.access import video_access


def theme_list_gen(video_list):
    themes = {}
    for video in video_list:
        if video_access.valid(video):
            theme = video['theme']
            score = video['thumb_up'] - video['thumb_down'] / 2
            themes[theme] = themes.get(theme, 0) + score
    return sorted(themes.items(), key=lambda item: -item[1])


@bp.route('/', methods=['GET', 'POST'])
def list():
    video_list = video_access.get_all()
    theme_list = theme_list_gen(video_list)
    return render_template('theme.html', items=theme_list)



