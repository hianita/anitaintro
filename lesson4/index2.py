from flask import Flask, render_template, request, redirect, url_for, session
app=Flask(__name__)
app.secret_key=b'\xcc\xdfU\xad#\xb2\n\xa9\xde\x1e\xe1|'
  
@app.route("/")
def index():
    return render_template("signin.html")
    
@app.route("/member")
def member():
    if session.get("user"):
        return render_template("member.html")
    else:
        return redirect("/")
    
@app.route("/error")
def error():
    return render_template("error.html")
   
@app.route("/signin",methods=["POST"])
def signin():
    if request.values["account"]=='test'and request.values["password"]=='test':
        session["user"]=request.values["account"]
        print(session["user"])
        return redirect("/member")
    else:
        return redirect("/error")
    
@app.route("/signout")
def signout():
    session.pop("user", None)
    return redirect(url_for("index"))
    
if __name__=="__main__":
    app.run(port='3000',debug=True)
    