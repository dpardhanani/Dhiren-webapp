from flask import Flask, render_template, render_template_string, request, redirect, url_for
from flask_mail import Mail, Message
from flask_socketio import SocketIO, join_room, leave_room
import random
import os
 
application = Flask(__name__)

# Only enable Flask debugging if an env var is set to true
# application.debug = os.environ.get('FLASK_DEBUG') in ['true', 'True']
application.debug = True

# Get application version from env
# app_version = os.environ.get('APP_VERSION')
app_version = 'Version 1.0'

# Get cool new feature flag from env
# enable_cool_new_feature = os.environ.get('ENABLE_COOL_NEW_FEATURE') in ['true', 'True']
enable_cool_new_feature = 'True'

@application.route('/')
def hello_world():
    message = "Hello, world!"
    return render_template('index.html',
                                  title=message,
                                  flask_debug=application.debug,
                                  app_version=app_version,
                                  enable_cool_new_feature=enable_cool_new_feature)

answers = ["It is certain",
           "It is decidedly so",
           "Without a doubt",
           "Yes - definitely",
           "You may rely on it",
           "As I see it, yes",
           "Most likely",
           "Outlook good",
           "Yes",
           "Signs point to yes",
           "Don't count on it",
           "My reply is no",
           "My sources say no",
           "Outlook not so good",
           "Very doubtful",
           "Reply hazy, try again",
           "Ask again later",
           "Better not tell you now",
           "Cannot predict now",
           "Concentrate and ask again"]

@application.route("/magic_8_ball", methods=['GET', 'POST'])
def eight_ball():
    return render_template("Magic_8_ball.html")

@application.route("/magic_8_ball/answer", methods=['GET', 'POST'])
def eight_ball_answer():
    random_c = random.choice(answers)
    return render_template("Magic_8_ball_answer.html", randomc=random_c)

socketio = SocketIO(application)
application.config['MAIL_SERVER'] = 'smtp.ipage.com'
application.config['MAIL_PORT'] = 465
application.config['MAIL_USE_TLS'] = False
application.config['MAIL_USE_SSL'] = True
# application.config['MAIL_DEBUG'] = True
application.config['MAIL_USERNAME'] = 'jahaan@fireballtechnologies.com'
application.config['MAIL_PASSWORD'] = 'Inventor2763223022forKidflash'
application.config['MAIL_DEFAULT_SENDER'] = "jahaan@fireballtechnologies.com"
application.config['MAIL_MAX_EMAILS'] = 10
# application.config['MAIL_SUPPRESS_SEND'] = False
application.config['MAIL_ASCII_ATTACHMENTS'] = False
mail = Mail(application)

@application.route("/feedback")
def feedback():
    return render_template("Feedback.html")

@application.route("/feedback/send-email", methods=['GET', 'POST'])
def feedback_send_email():
    Name = request.form.get("Name")
    Email = request.form.get("Email")
    Feedback_message = request.form.get("Message")
    Feedback_subject = 'Website feedback from ' + Name + ', ' + Email

    msg = Message(Feedback_subject, recipients=[
                  "jahaan@fireballtechnologies.com"], body=Feedback_message)
    mail.send(msg)
    return "Thank you for your feedback!"

@application.route("/message_codifier/encrypt")
def encrypt():
    return render_template("Encrypt.html")

@application.route("/message_codifier/encrypt/check", methods=['GET', 'POST'])
def encrypt_check():
    message = request.form.get("message")
    e_m = encrypt_message(message)

    return render_template("Encrypt.html", encrypted_message=e_m)

def encrypt_message(message):
    encrypted_message = ""
    for i in message:
        calc1 = ord(i)
        calc2 = calc1 + 5
        calc3 = chr(calc2)
        encrypted_message = encrypted_message + calc3
    return encrypted_message

@application.route("/message_codifier/decrypt")
def decrypt():
    return render_template("Decrypt.html")

@application.route("/message_codifier/decrypt/check", methods=['GET', 'POST'])
def decrypt_check():
    message = request.form.get("message")
    d_m = decrypt_message(message)

    return render_template("Decrypt.html", decrypted_message=d_m)

def decrypt_message(message):
    decrypted_message = ""
    for i in message:
        calc1 = ord(i)
        calc2 = calc1 - 5
        calc3 = chr(calc2)
        decrypted_message = decrypted_message + calc3
    return decrypted_message

@application.route("/chat")
def chat():
    return render_template("Chat_setup.html")

@application.route("/chat/room")
def chat_room():
    username = request.args.get('username')
    room = request.args.get('room')
    if username and room:
        if check_if_firetech_user(username, room) == True:
            # return redirect("/chat/room/firetech")
            return render_template("Chat_FireTech.html", username=username, room=room)
        else:
            return render_template("Chat_FireTech.html", username=username, room=room)

@application.route("/chat/room/firetech")
def chat_room_firetech():
    username = request.args.get('username')
    room = request.args.get('room')
    if username and room:
        if check_if_firetech_user(username, room) == True:
            return redirect("/chat/room/firetech")
            return render_template("Chat_FireTech.html", username=username, room=room)
    else:
        return redirect(url_for('chat'))

usernames = [
    "JahaanP",
    "gemarshdeep15",
    "Kaveeshmi",
    "sonic_crusher2823",
    "Sahil",
    "epicdragonwolf101",
    "Naisha"]

def check_if_firetech_user(username, room):
    firetech = "FireTech"
    if room.lower() == firetech.lower():
        try:
            isUsernameInList = username in usernames
            return True
        except:
            return False
    else:
        return False

@socketio.on('send_message')
def handle_send_message_event(data):
    application.logger.info("{} has sent: {}".format(
        data['username'], data['message']))
    join_room(data['room'])
    socketio.emit('receive_message', data, room=data['room'])

@socketio.on('join_room')
def handle_join_room_event(data):
    application.logger.info("{} has joined the room {}".format(
        data['username'], data['room']))
    join_room(data['room'])
    socketio.emit('join_room_announcement', data)

@socketio.on('leave_room')
def handle_join_room_event(data):
    application.logger.info("{} has left the room {}".format(
        data['username'], data['room']))
    join_room(data['room'])
    socketio.emit('leave_room_announcement', data)

if __name__ == '__main__':
#    application.run(host='0.0.0.0')
    socketio.run(application, debug=True)