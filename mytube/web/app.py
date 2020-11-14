from flask import Flask

app = Flask(__name__)

from view.video import bp as video_bp
from view.theme import bp as theme_bp

app.register_blueprint(video_bp, url_prefix='')
app.register_blueprint(theme_bp, url_prefix='/theme')

if __name__ == '__main__':
    app.run(threaded=True, port=1818)