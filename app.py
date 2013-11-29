from flask import Flask, render_template, url_for, redirect, request, session
import auth

app = Flask(__name__)
app.secret_key = 'secretkey'

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method=="GET":
        return render_template('login.html')
    else:
        username = request.form["username"].encode("ascii","ignore")
        password = request.form["password"].encode("ascii","ignore")
        if (auth.authenticate(username,password)):
            session["username"] = username
            return redirect(url_for("portfolio"))
        else:
            return redirect(url_for("register"))

            @app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form["username"].encode("ascii","ignore")
        password = request.form["password"].encode("ascii","ignore")
        if (auth.register(username,password)):
            session["username"] = username
            return redirect(url_for("login")) #login after registering or log in automatically?
        else:
            return redirect(url_for("register")) #return specific error?

@app.route("/portfolio")
def portfolio():
    if auth.logged_in():
        return render_template("portfolio.html")
    else:
        return redirect(url_for("login"))

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "GET":
        return render_template("search.html")
    else:
        search = request.form["search"]
        return auth.search(search) 

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("home"))
    
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=5000)
