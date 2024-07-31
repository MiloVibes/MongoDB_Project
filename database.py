from pymongo import MongoClient
from bson import ObjectId
import json
from datetime import datetime

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime):
            return o.isoformat()
        return super(JSONEncoder, self).default(o)
    
client = MongoClient("mongodb://localhost:27017/")
db = client.catalogDB
collection = db.items

def insert_item(item):
    return collection.insert_one(item)

def update_item(query, new_values):
    collection.update_one(query, {"$set": new_values})

def delete_item(query):
    collection.delete_one(query)

def get_items():
    items = list(collection.find())
    for item in items:
        item['_id'] = str(item['_id'])
        if 'date' in item:
            item['date'] = item['date'].strftime('%Y-%m-%d') if isinstance(item['date'], datetime) else item['date']
    return items
