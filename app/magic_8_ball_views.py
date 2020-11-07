from app import app
from flask import render_template
import random

# Magic 8 Ball
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

@app.route("/magic_8_ball", methods=['GET', 'POST'])
def eight_ball():
    return render_template("Magic_8_ball.html")

@app.route("/magic_8_ball/answer", methods=['GET', 'POST'])
def eight_ball_answer():
    random_c = random.choice(answers)
    return render_template("Magic_8_ball_answer.html", randomc=random_c)

