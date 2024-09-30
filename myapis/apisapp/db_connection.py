import pymongo

url = 'mongodb+srv://ushindigideon01:%40mongodb2024@cluster0.lc4qeak.mongodb.net/'
client = pymongo.MongoClient(url)
db = client['blog']