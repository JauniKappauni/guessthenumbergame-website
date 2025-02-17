from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def function1():
    randomnumb = random.randint(0, 100)
    output = ""
    if request.method == "POST":
        number = int(request.form.get("number"))
        if number > randomnumb:
            output = "❌" + "Try again. The number is lower than that"
        elif number < randomnumb:
            output = "❌" + "Try again. The number is higher than that"
        else:
            output = "✅" + f"{number} was the correct number"
    return render_template("index.html", output=output)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=20012, debug=True)