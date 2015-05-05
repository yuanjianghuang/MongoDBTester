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

    document_sample = collection.find_one({'url': "http://www.rongmofang.com/information/infolist?infotype=1&page=0"} )
    if not document_sample:
        print "no document found."
    else:
        print "document found,and has text: ", document_sample['text']
        print "document found,and has internal url: ", document_sample['url_internal']
        print "document found,and has external url: ", document_sample['url_external']

if __name__ == "__main__":
    main()
