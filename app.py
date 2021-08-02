from flask import Flask,render_template

app=Flask(__name__)

@app.route("/hi")

def hello():
    return render_template("index.html")


app.run()

    