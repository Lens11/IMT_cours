from pymongo import MongoClient
import datetime
import re

client = MongoClient()
mydb = client.new_york
#mydb = client ['test_database_1'] On peut faire ça aussi, c'est le "dictionary style"
my_collection = mydb.restaurants
restaurant_count = mydb.restaurants.count_documents({})
print(restaurant_count)

# Afficher les clés (colonnes) du document échantillon
def afficher_colonne():
    sample_document = my_collection.find_one()
    colonnes = list(sample_document.keys())
    print(colonnes)

### Question 1 ###

def choix_restaurant(id=None, name=None, borough=None):
    query = {}
    or_conditions = []

    if id is not None:
        or_conditions.append({'_id': id})
    if name is not None:
        or_conditions.append({'name': name})
    if borough is not None:
        or_conditions.append({'borough': borough})
    
    if or_conditions:
        query['$or'] = or_conditions #'$or' permet de retourner qqch qui correspondent à au moins l'une de ces conditions.
    
    resultat = my_collection.find_one(query,{"name":1, "_id":0})
    return resultat["name"]
    # for restaurant in resultat:
    #     return (restaurant) Si j'avais utilisé .find()
    
    #return mydb.restaurants.find({"name" : "nom"},{"name":1, "_id":1, "borough":1}) or 
    # for restaurant in choix:
    #     print (restaurant)
    # return restaurant


#print(choix_restaurant(name = "Joe'S Pizza"))



### Question 2 ###
    
def lister_noms_restaurants():
    restaurants = my_collection.find({}, {"name": 1, "_id": 0}).sort("name", 1) #On va trier par nom (ascendant)
    return [restaurant['name'] for restaurant in restaurants]

# Appeler la fonction et afficher les résultats
def liste_nom():
    noms_restaurants = lister_noms_restaurants()
    for nom in noms_restaurants:
        print(nom)
    
### Question 3 ### Write a python function that adds a new restaurant to the collection
def insertion (name, borough):     
    record_id = my_collection.insert_one(myrecord)
    print(record_id)


