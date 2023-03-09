from flask import Flask, request 
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps
from models import Scheme, Paint, Area, Step
from flask_cors import CORS
from client import clientUrl

app = Flask(__name__)
CORS(app)

# Create a folder called client.py
# Declare clientUrl as a variable to the path for your MongoDB database

client = MongoClient(clientUrl)

db = client.PaintApp

schemes = db.Schemes
allPaints = db.Paints


@app.route('/allschemes', methods = ['POST', 'GET'])
def allschemes():

    if request.method == 'POST':
        pass

    allSchemesCursor = schemes.find()
    listAllSchemes = list(allSchemesCursor)
    jsonAllSchemes = dumps(listAllSchemes)

    return jsonAllSchemes

@app.route('/scheme/<id>')
def scheme(id):


    foundScheme = schemes.find_one(ObjectId(id))
    jsonScheme = dumps(foundScheme)

    return jsonScheme

@app.route('/paints')
def paints():

    allPaintsCursor = allPaints.find()
    listAllPaints = list(allPaintsCursor)
    jsonAllPaints = dumps(listAllPaints)

    return jsonAllPaints

@app.route('/step', methods = ['POST'])
def step():
    schemeId = request.json['schemeId']
    areaName = request.json['areaName']
    paint = request.json['paint']
    type = request.json['type']
    method = request.json['method']

    query = {'_id': ObjectId(schemeId)}
    update = {'$push': {'areas.$[n].steps': {'method': method, 'paint': paint}}}
    filter = [{'n.name': areaName}]

    schemes.update_one(query, update, array_filters=filter)

    foundScheme = schemes.find_one(ObjectId(schemeId))
    jsonScheme = dumps(foundScheme)

    return jsonScheme




if __name__ == '__main__':
    app.run(debug = True)