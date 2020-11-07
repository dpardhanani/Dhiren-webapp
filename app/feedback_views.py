from app import app
from flask import render_template, request, redirect, url_for, session
from flask_mail import Mail, Message

mail = Mail(app)

@app.route("/feedback")
def feedback():
    return render_template("Feedback.html")

@app.route("/feedback/send-email", methods=['GET', 'POST'])
def feedback_send_email():
    Name = request.form.get("Name")
    Email = request.form.get("Email")
    Feedback_message = request.form.get("Message")
    Feedback_subject = 'Website feedback from ' + Name + ', ' + Email

    msg = Message(Feedback_subject, recipients=[
                  "jahaan@fireballtechnologies.com"], body=Feedback_message)
    mail.send(msg)
    return "Thank you for your feedback!"