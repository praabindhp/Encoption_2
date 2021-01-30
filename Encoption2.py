from flask import Flask, render_template, request
from flask_pymongo import PyMongo
from decouple import config
from bson.json_util import dumps
import random
app=Flask(__name__)

app.config["MONGO_URI"]=config("MONGO_URI")
mongo=PyMongo(app)
Encoption=mongo.db.Random_List

@app.route('/', methods=["POST","GET"])
def search():
    return render_template("show.html")

@app.route('/show', methods=["POST","GET"])
def show():
    #names={"Hale", "Zephox", "Alphox", "Hampy", "Toller", "Dupper", "Senter"}
    #n=random.randint(0, len(names))
    #print(n)
    #print(names[n])

    Name=request.form.get("name")
    #data=Encoption.find({"Name":Name})
    data=Encoption.aggregate([{"$sample": {"size":1}}])
    return render_template("show.html",data=data,name=Name)

@app.route('/add')
def Encoption_main():
    return render_template('Encoption_Temp.html')

@app.route('/insert', methods=["POST"])
def Encoption_add():
    dicts={
        "Name":request.form.get("name"),
        "Nick_Name":request.form.get("nickname")
    }
    res=Encoption.insert_one(dicts)
    print(res)
    return render_template('Encoption_Temp.html')

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)