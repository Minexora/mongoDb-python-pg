import json
from time import sleep
from datetime import datetime
from mongo import MongoDBProgress

start_time = datetime.now().strftime('%m/%d/%Y-%H:%M:%S')

print("Dosyadan veriler okunuyor.")
file = open('example.json')
data = json.load(file)

end_time = datetime.now().strftime('%m/%d/%Y-%H:%M:%S')
print("Dosyadan okunana dataya tarih değerleri ekleniyor.")
data["start_time"] = start_time
data["end_time"] = end_time


print("Veriler MongoDb'ye gönderiliyor.")
mongo_ref = MongoDBProgress()
res = mongo_ref.insert_data_to_collection(
    database_name="Sandbox",
    collection_name="USER_FOR_SANDBOX",
    data=data
)

print(f"Kayıt eklendi. Kayıt id: {res}")


sleep(30)

_query = {"name": "Giray"}

mongo_ref.delete_data_to_collection(
    database_name="Sandbox",
    collection_name="USER_FOR_SANDBOX",
    query=_query
)
