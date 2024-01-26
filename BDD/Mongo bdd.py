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

