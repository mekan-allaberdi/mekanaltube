from . import db
from bson.objectid import ObjectId

ID = '_id'
NAME = 'name'
THEME = 'theme'
THUMB_UP = 'thumb_up'
THUMB_DOWN = 'thumb_down'

VIDEO_KEYS = [NAME, THEME, THUMB_UP, THUMB_DOWN]


def valid(video):
    for key in VIDEO_KEYS:
        if video.get(key, None) is None:
            return False
    else:
        return True


def get(id):
    print(id)
    return db.video.find_one({ID: ObjectId(id)})


def upvote(id):
    video = get(id)
    thumb_ups = video[THUMB_UP] + 1
    db.video.update_one({ID: ObjectId(id)}, {"$set": {THUMB_UP: thumb_ups}})


def downvote(id):
    video = get(id)
    thumb_ups = video[THUMB_DOWN] + 1
    db.video.update_one({ID: ObjectId(id)}, {"$set": {THUMB_DOWN: thumb_ups}})


def create(name, theme):
    new_video = {
        NAME: name,
        THEME: theme,
        THUMB_UP: 0,
        THUMB_DOWN: 0
    }
    db.video.insert_one(new_video)


def get_all():
    return [{'name': 'Eziz',
            'theme': 'film',
            'thumb_up': 1,
            'thumb_down': 2}]
    return list(db.video.find({}))

