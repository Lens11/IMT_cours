from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import json_util, ObjectId



app = Flask(__name__)
client = MongoClient('localhost',27017)

db = client.new_york.restaurants

@app.route('/')
def index():
    return "Bienvenue sur l'API Rest des restaurants! Tapez /restaurants"

@app.route('/restaurants', methods=['GET'])
def choix_restaurant():
    filtre = {}
    
    # Récupérer les paramètres de la requête GET
    id = request.args.get('id')
    name = request.args.get('name')
    borough = request.args.get('borough')
    cuisine = request.args.get('cuisine')
    grades = request.args.get('grades')
    
    # Construire le filtre
    if id is not None:
        filtre['restaurant_id'] = id  # Convertir en ObjectId pour la recherche par _id dans MongoDB
    if name is not None:
        filtre['name'] = name
    if borough is not None:
        filtre['borough'] = borough
    if cuisine is not None:
        filtre['cuisine'] = cuisine
    if grades is not None:
        filtre['grades'] = grades
        
    # Exécution de la requête sur la base de données
    resultat = db.find(filtre,{"_id":0})
    
    # Convertir les résultats en une liste de JSON
    resultat_liste = list(resultat)
    return jsonify(resultat_liste)
    #return json_util.dumps()

#@app.route('/restaurants/<id>', methods=['POST'])


if __name__ == '__main__':
    app.run(debug=True)