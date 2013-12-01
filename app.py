from flask import Flask, render_template, url_for, redirect, request, session
import utils
import auth

app = Flask(__name__)
app.secret_key = 'secretkey'

@app.route("/")
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    else:
        return render_template('home.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        if (auth.login(username,password)):
            session["username"] = username
            return render_template('home.html', username=session['username'])
        else:
            return redirect(url_for("login"))

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        if auth.register(username,password):
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return render_template("register.html") #return specific error?

@app.route("/portfolio")
def portfolio():
    if 'username' in session:
        user = session['username']
        return render_template("portfolio.html",username = user,cash=auth.getCash(user), stocks = auth.getStocks(user))
    else:
        return render_template("portfolio.html")
    
@app.route("/buynsell")
def buynsell():
    if request.method == "GET":
        if 'username' in session:
            return render_template("buynsell.html", username = session['username'])
        else:
            return render_template('buynsell.html')
    else:
        symb = request.form['symbol']
        num = request.form['number']
        action = request.form['action']
        user = session['username']
        if action == 'buy':
            auth.buy(session['username'], symb, num)
            return render_template('portfolio.html', username = user, cash=auth.getCash(user), stocks = auth.getStocks(user))
        else:
            auth.sell(session['username'], symb, num)
            return render_template('portfolio.html', username = user, cash=auth.getCash(user), stocks = auth.getStocks(user))

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "GET":
        if 'username' in session:
            return render_template("search.html",username = session["username"])
        else:
            return render_template("search.html")
    else:
        symb = request.form['symb']
        q = utils.init(symb)
        if 'username' in sesssion:
            return render_template("stocks.html",username = session["username"], q=q)
        else:
            return render_template("stocks.html", q=q)

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("home"))
    
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=5000)
