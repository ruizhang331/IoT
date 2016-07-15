from pymongo import MongoClient
from random import randint
from datetime import datetime

try:
    client = MongoClient()
    db = client.test_database
    collection = db.test_collection
    sensor_data = db.sensor_data
    #fake data generation
    sensor_data.insert(dict(date=datetime.now(), value=randint(1, 100)))
    # query mongo DB with data between start and end time, and value smaller than certain threhold 
    now = datetime.now()
    start = now.replace(hour=8, minute=0, second=0, microsecond=0)
    end = datetime.strptime("14/07/16 16:30", "%d/%m/%y %H:%M")

    for data_reading in sensor_data.find({"$and": [{'date':{"$gt":start,'$lt':now}},{"value": {"$lt": 50}}]}).sort("value"):
        print data_reading


except pymongo.errors.ConnectionFailure, e:
   print "Could not connect to MongoDB: %s" % e 

