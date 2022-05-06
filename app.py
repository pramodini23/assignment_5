from flask import Flask,jsonify, render_template, request, redirect,url_for,escape
import json


app = Flask(__name__)
jData = json.loads(open('./customers.json').read())
data=jData["customers"]

@app.route('/')
def car_main():
    return render_template("index.html")

@app.route('/customers/')
def getAllcustomers():
    myList=[]
    for element in data:
        myList.append(element)
    result = jsonify(myList)
    return render_template("index.html",items=myList)

@app.route('/customers/<string:Year>/')
def getyear(Year=''):
    myList=[]
    for element in data:
        if element["Year"] == Year:
            myList.append(element)
    result = jsonify(myList)
    return render_template("index.html",items=myList)


@app.route('/customers/year/<string:Year>/<string:ID>')
def getBank(Year, ID):
    myList=[]
    for element in data:
        if element["Year"]== Year:
            if element ["Bank"] == ID:
                myList.append(element)
    result = jsonify(myList)
    return render_template("index.html",items=myList)

@app.route('/customers/<string:Bank>/<string:AccountNumber>')
def getAccountNumber(AccountNumber,Bank):
    print AccountNumber + Bank
    myList=[]
    for element in data:
        if element ["Bank"] == Bank:
            if element ['AccountNumber'] == AccountNumber:
                myList.append(element)
    result = jsonify(myList)
    return render_template("index.html",items=myList)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')