from flask import Flask

app = Flask(__name__)

from app import magic_8_ball_views
from app import todo_views
from app import login_views
from app import feedback_views
'''
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "Jahaan"
app.config['MAIL_SERVER'] = 'smtp.ipage.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
# app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = 'jahaan@fireballtechnologies.com'
app.config['MAIL_PASSWORD'] = 'Inventor2763223022forKidflash'
app.config['MAIL_DEFAULT_SENDER'] = "jahaan@fireballtechnologies.com"
# app.config['MAIL_SUPPRESS_SEND'] = False
app.config['MAIL_ASCII_ATTACHMENTS'] = False
'''

app.config["SECRET_KEY"] = "Jahaan"
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
#app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = True
#app.config['MAIL_USE_SSL'] = True
#app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = 'dpardhanani@gmail.com'
app.config['MAIL_PASSWORD'] = 'jzdnjxgffkonzdox'
app.config['MAIL_DEFAULT_SENDER'] = "dpardhanani@gmail.com"
#app.config['MAIL_MAX_EMAILS'] = 10
# app.config['MAIL_SUPPRESS_SEND'] = False
#app.config['MAIL_ASCII_ATTACHMENTS'] = False
