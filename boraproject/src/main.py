from flask import *

app = Flask(__name__)
app.secret_key = "anshid"

@app.route("/", methods=['get', 'post'])
def main():
    return render_template("index.html")

@app.route("/home", methods=['get', 'post'])
def home():
    return render_template("index.html")

@app.route("/about", methods=['get', 'post'])
def about():
    return render_template("about.html")

@app.route("/profit", methods=['get', 'post'])
def profit():
    amount=int(request.form['amount'])
    perc=float(request.form['perc'])
    days = int(request.form['days'])
    profit = 0
    tprofit=0
    i = 0
    am=amount
    while (i<days):
        profit = (perc / 100) * amount  #
        amount += profit
        tprofit = tprofit + profit
        i = i + 1

    return render_template("index.html",am=am,perc=perc,val=amount,val1=tprofit,val2=days)




if __name__ == "__main__":
    app.run(debug=True)