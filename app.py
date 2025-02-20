from flask import Flask, render_template, request, session
import random
import os

app = Flask(__name__)
app.secret_key = os.urandom(16)

@app.route("/", methods=["GET", "POST"])
def function1():
    if "randomnumb" not in session:
        session["randomnumb"] = random.randint(0, 100)
    randomnumb = session["randomnumb"]
    number = 0
    output = ""
    if request.method == "POST":
        if "reset" in request.form:
            session.pop("randomnumb", None)
            session["randomnumb"] = random.randint(0, 100)
            output = "Number to be guessed was reset. Please refresh the website!"
        else:
            number = int(request.form.get("number"))
            if number > randomnumb:
                output = "❌ Try again. The number is lower than that"
            elif number < randomnumb:
                output = "❌ Try again. The number is higher than that"
            else:
                output = "✅ " + f"{number} was the correct number"
    
    return render_template("index.html", randomnumb=randomnumb, number=number, output=output)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=20012, debug=True)