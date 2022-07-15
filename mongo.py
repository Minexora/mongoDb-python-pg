import pymongo
import traceback


class MongoDBProgress:
    mongo_client = None
    database_ref = None
    collection_ref = None

    def __init__(self) -> None:
        try:
            self.mongo_client = pymongo.MongoClient(
                "mongodb://sandbox:deneme12@localhost:27017/")
        except Exception:
            print(traceback.format_exc())

    def check_database(self, database_name):
        return database_name in self.mongo_client.list_database_names()

    def check_collection_name(self, collection_name):
        return collection_name in self.database_ref.list_collection_names()

    def create_database(self, database_name):
        self.database_ref = self.mongo_client[database_name]

    def create_collection(self, database_name=None, collection_name=None):
        if not self.database_ref:
            self.create_database(database_name=database_name)
        self.collection_ref = self.database_ref[collection_name]

    def insert_data_to_collection(self, database_name="Sandbox", collection_name=None, data={}):
        if not self.collection_ref:
            self.create_collection(
                database_name=database_name,
                collection_name=collection_name
            )
        res = self.collection_ref.insert_one(data)
        return res.inserted_id

    def delete_data_to_collection(self, query, database_name="Sandbox", collection_name=None):
        res = self.collection_ref.delete_one(query)
