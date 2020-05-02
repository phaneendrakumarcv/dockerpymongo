from flask import Flask
from flask import request
from pymongo import MongoClient
from flask_pymongo import PyMongo
import os

app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb://localhost:27017/database"

conn = MongoClient(host='mongo', port=27017) 
db = conn["database"]
coll = db["laptop_collection"]

db= conn.database

@app.route('/')
def hello():
    return 'Hello world'

@app.route('/insert',methods=["POST"])
def insertData():
    req_data = request.get_json()
    brand = req_data['brand']
    model = req_data['model']
    cost = req_data['cost']
    record = {
        "brand":brand,
        "model":model,
        "cost":cost
    }

    inserted_record = coll.insert_one(record)

    return str(inserted_record.inserted_id)



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5001,debug=True)