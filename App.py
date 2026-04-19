from flask import Flask, render_template, request

app = Flask(__name__)

numbers = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        num = int(request.form["num"])
        numbers.append(num)

    total = sum(numbers)

    return render_template("index53.html", numbers=numbers, total=total)

if __name__ == "__main__":
    app.run(debug=True)
