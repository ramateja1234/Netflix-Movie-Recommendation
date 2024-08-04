from flask import Flask , render_template , request

import netflix

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route("/sub",methods=['POST'])
def submit():
    if request.method=="POST":
        name=request.form["username"]
        display=netflix.get_recommendations(name)
    return render_template("sub.html",n = display)
if __name__ == '__main__':
    app.run(debug=True)