from flask import Flask

app = Flask(__name__)

from app import magic_8_ball_views