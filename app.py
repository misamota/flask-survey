from flask import Flask, request, render_template, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey


app = Flask(__name__)
app.config["secret_key"] = "something"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


debug = DebugToolbarExtension(app)
@app.route("/")
def survey_start():

    return render_template("survey_start.html"survey=survey)

@app.route("/answer",methods=["POST"])
def answer_questions():

    session[RESPONSES_KEY] = []

    return redirect("/questions/0")

@app.route("/answer",methods=["POST"])
def handle_question():

    choice = request.form["answer"]

    responses = session[RESPONSE_KEY]
    responses.append(choice)
    session[RESPONSES_KEY] = responses

    if(len(responses) == len(survey.questions)):

        return redirect("/complete")
    else:
        return redirect(f"/questions/{len(responses)}")

@app.route("/questions/<int:qid>")
def show_question(qid):

    if (responses is None):
        # trying to access question page too soon
        return redirect("/")

    if (len(responses) == len(survey.questions)):
        # They've answered all the questions! Thank them.
        return redirect("/complete")

    if (len(responses) != qid):
        # Trying to access questions out of order.
        flash(f"Invalid question id: {qid}.")
        return redirect(f"/questions/{len(responses)}")

    question = survey.questions[qid]
    return render_template(
        "question.html", question_num=qid, question=question)




@app.route("/finished")
def finished():
    """shows comletion page"""
    return render_template("completion.html")
    