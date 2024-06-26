import requests
import os
from todo_app.data.item import Item
from todo_app.data.status import Status, get_list_id

def get_items_from_trello():
    """
    Fetches all saved items from TRELLO list.

    Returns:
        list: The list of saved items.
    """
    
    url = f'https://api.trello.com/1/boards/{os.getenv("TRELLO_BOARD_ID")}/cards'
    query = {
        'key' : os.getenv("TRELLO_API_KEY"),
        'token' : os.getenv("TRELLO_API_TOKEN"),
    }
    response = requests.request("GET", url, params=query)
    return [ Item.from_trello_card(card) for card in response.json()]

def add_item_to_trello(name):
    """
    Adds a new item with the specified title to TRELLO "To do" list.

    Args:
        name: The name of the item.
    """

    url = "https://api.trello.com/1/cards"
    query = {
        'key': os.getenv("TRELLO_API_KEY"),
        'token': os.getenv("TRELLO_API_TOKEN"),
        'name':name,
        'idList': get_list_id(Status.TO_DO),
    }
    requests.request(
        "POST",
        url,
        params=query
    )

    
def change_status_of_item_on_trello(id, status: Status):
    """
    Moves item with provided id to the list for the desired status.

    Args:
        id: The id of the item.
        status: The desired new status of the item.

    """

    url = f'https://api.trello.com/1/cards/{id}'
    query = {
        'key': os.getenv("TRELLO_API_KEY"),
        'token': os.getenv("TRELLO_API_TOKEN"),
        'idList': get_list_id(status),
    }
    requests.request(
        "PUT",
        url,
        params=query
    )