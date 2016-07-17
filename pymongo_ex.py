from pymongo import MongoClient
import pymongo
from random import randint
from datetime import datetime

'''
Example of how to use mongo DB to manipulate IoT device data.
1. IoT device generate data as {time:value} pairs.
2. Use Mongodb to query the data based on time stamp and value
'''

try:
    client = MongoClient()
    db = client.test_database
    collection = db.test_collection
    sensor_data = db.sensor_data
    result_add = sensor_data.insert(dict(date=datetime.now(), value=randint(1, 100)))

    now = datetime.now()
    start = now.replace(hour=8, minute=0, second=0, microsecond=0)
    #end = datetime.strptime("14/07/16 16:30", "%d/%m/%y %H:%M")
    yesterday = now.replace(hour=0, minute=0, second=0, microsecond=0)
    #delete all sensor data before today
    result_delete = sensor_data.delete_many({'date':{'$lt':yesterday}})
    print sensor_data
    #query data between today 8am until now, and value smaller than 50 in descending sorted way
    for data_reading in sensor_data.find({"$and": [{'date':{"$gt":start,'$lt':now}},{"value": {"$lt": 50}}]}).\
        sort("value",pymongo.DESCENDING):
        print data_reading


except pymongo.errors.ConnectionFailure, e:
   print "Could not connect to MongoDB: %s" % e 

