from flask import Flask, render_template, request
from tool1 import extract_keywords
import os
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    keywords = None
    
    if request.method == "POST":
        text = request.form["text"]
        keywords = extract_keywords(text, 5)

    return render_template("index.html", keywords=keywords)


if __name__ == "__main__":
    port=int(os.environ.get("PORT",10000))
    app.run(debug=True)

