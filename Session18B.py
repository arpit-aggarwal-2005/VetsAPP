import pymongo
from tabulate import tabulate

class MongoDBHelper:

    def __init__(self, collection='customer'):
        uri = "mongodb+srv://aaggarwal1_be22:KK2yAEfWsNUNOk7U@cluster0.2c1ucxn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        client = pymongo.MongoClient(uri)
        self.db = client['VetsApp']
        self.collection = self.db[collection]
        print("MongoDB Connected")

    def insert(self, document):
        result = self.collection.insert_one(document)
        print("Document Inserted:", result)
        # result.inserted_id -> Document Id
        return result

    def delete(self, query):
        result = self.collection.delete_one(query)
        print("Document Deleted:", result)

    def fetch(self, query=""):
        documents = self.collection.find(query) # find_one()
        return list(documents)

    def update(self, document, query):
        update_query = {'$set': document}
        result = self.collection.update_one(query, update_query)
        print("Updated Document:", result.modified_count)
