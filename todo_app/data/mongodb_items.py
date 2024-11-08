import pymongo
import os
from todo_app.data.item import Item
from todo_app.data.status import Status, get_status_from_string, get_string_from_status

def get_items_collection():
    """
    Gets the database collection from the 
    """
    client = pymongo.MongoClient(os.getenv("COSMOSDB_CONNECTION_STRING"))
    database = client[os.getenv("DATABASE_NAME")]
    collection = database[os.getenv("ITEMS_COLLECTION_NAME")]

    return collection

def get_items_from_mongodb():
    """
    Fetches all saved items from MongoDB.

    Returns:
        list: The list of saved items.
    """

    collection = get_items_collection()
    items = collection.find()

    return [ Item.from_database_item(item) for item in list(items) ]

def add_item_to_mongodb(name):
    """
    Adds a new item with the specified title to MongoDB with status 'To do'.

    Args:
        name: The name of the item.
    """

    item = {
        'name': name,
        'status': get_string_from_status(Status.TO_DO)
    }

    collection = get_items_collection()
    collection.insert_one(item)
    
def change_status_of_item_on_mongodb(id, status: Status):
    """
    Moves item with provided id to the list for the desired status.

    Args:
        id: The id of the item.
        status: The desired new status of the item.

    """

    collection = get_items_collection()

    collection.update_one({'_id': str(id)}, {'$set' :{'status': get_string_from_status(status)}})