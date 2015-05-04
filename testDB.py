from pymongo import MongoClient
import sys
from pymongo.errors import ConnectionFailure

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "ronmofangDB"
MONGODB_COLLECTION = "ronmofangCollection"
# This py is used to test Mongo database related issues.
def main():
    try:
        connection = MongoClient(
            MONGODB_SERVER,
            MONGODB_PORT
        )
        db = connection[MONGODB_DB] # Getting a databse
        collection = db[MONGODB_COLLECTION]  # Getting a collection
    except ConnectionFailure, e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)

    text = collection.find_one({'url': 'http://www.rongmofang.com/home/huifushenglibao'} )
    if not text:
        print "no document found."
    else:
        print "document found,and has internal url: ", text['url_internal']

if __name__ == "__main__":
    main()
