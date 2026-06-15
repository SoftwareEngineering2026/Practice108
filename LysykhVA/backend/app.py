from flask import Flask, request, jsonify
import os
import time

app = Flask(__name__)

from flask import Flask, request, jsonify
import os
import time

app = Flask(__name__)


def save_task(text, filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)


@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.json
    text = data["text"]

    save_task(text, "/data/task.txt")

    while not os.path.exists("/data/result.txt"):
        time.sleep(1)

    with open("/data/result.txt", "r", encoding="utf-8") as f:
        result = f.read()

    os.remove("/data/result.txt")

    return jsonify({
        "result": result
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )