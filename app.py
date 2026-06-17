from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        try:
            number = int(request.form["number"])

            if number % 2 == 0:
                result = f"{number} is Even"
            else:
                result = f"{number} is Odd"

        except ValueError:
            result = "Please enter a valid number"

    return f"""
    <html>
    <head>
        <title>Even or Odd Checker</title>
    </head>
    <body style="font-family: Arial; text-align:center; margin-top:50px;">
        <h1>Even or Odd Checker</h1>

        <form method="POST">
            <input type="number" name="number" placeholder="Enter a number" required>
            <button type="submit">Check</button>
        </form>

        <h2>{result}</h2>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
