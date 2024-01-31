from pymongo import MongoClient
import datetime
import re

client = MongoClient()
mydb = client.new_york
#mydb = client ['test_database_1'] On peut faire ça aussi, c'est le "dictionary style"
my_collection = mydb.restaurants

#databases = client.list_database_names()  #Cela liste toutes les bases de données

restaurant_count = mydb.restaurants.count_documents({})
print(restaurant_count)

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
    return resultat
    # for restaurant in resultat:
    #     return (restaurant) Si j'avais utilisé .find()
    
    #return mydb.restaurants.find({"name" : "nom"},{"name":1, "_id":1, "borough":1}) or 
    # for restaurant in choix:
    #     print (restaurant)
    # return restaurant


print(choix_restaurant(name = "Joe'S Pizza")["name"])



### Question 2 ###