from flask import Flask, request, render_template

app = Flask(__name__)
app.debug=True


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/myWorks")
def myWorks():
    return render_template("myWorks.html")

@app.route("/myResume")
def myResume():
    return render_template("myResume.html")

app.run(host='0.0.0.0', port=443)
