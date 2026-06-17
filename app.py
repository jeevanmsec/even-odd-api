from flask import Flask, jsonify, request

app = Flask(__name__)

def is_even(number):
    return number % 2 == 0

@app.route("/")
def home():
    return jsonify({"message": "Even/Odd Checker API"})

@app.route("/check")
def check():
    try:
        number = int(request.args.get("number"))

        return jsonify({
            "number": number,
            "result": "Even" if is_even(number) else "Odd"
        })

    except:
        return jsonify({"error": "Enter a valid number"}), 400

if __name__ == "__main__":
    app.run()
