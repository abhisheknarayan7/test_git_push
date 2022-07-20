import pymongo
client = pymongo.MongoClient("mongodb+srv://anarayan:sonu1983$@narayan.dccxw.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)


d = {
    "name":"abhishek",
    "emailid":"abhisheknarayan73@gmail.com",
    "surname":"narayan"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)