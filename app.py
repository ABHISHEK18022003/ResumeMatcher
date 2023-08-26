from flask import Flask, render_template, request
import matcher

app=Flask(__name__)



@app.route("/", methods = ["GET","POST"])
def index():
    m=""
    if request.method == "POST":
        resume=request.form["Resume"]
        job_desc=request.form["Job Description"]
        mat = matcher.match_predict(resume,job_desc)
        m=str(mat)
    return render_template("index.html",my_match=m)

if __name__ =="__main__":
    app.run()


