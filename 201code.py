from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "marks.html",
    )

@app.route("/s1", methods=["POST"])
def calc():
    if request.method == "POST":
        username = request.form["user"]
        marks = int(request.form["number"])

        if marks >= 90:
            return "A"

if __name__ == "__main__":
    app.run(debug=True, port=8003)