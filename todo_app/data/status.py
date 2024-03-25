import os
from enum import Enum

class Status(Enum):
    TO_DO = "To do"
    DOING = "Doing"
    DONE = "Done"

status_list_id = {
    Status.DONE: os.getenv("TRELLO_DONE_LIST_ID"),
    Status.DOING: os.getenv("TRELLO_DOING_LIST_ID"),
    Status.TO_DO: os.getenv("TRELLO_TO_DO_LIST_ID"),
}

list_id_status = {
    os.getenv("TRELLO_DONE_LIST_ID"): Status.DONE,
    os.getenv("TRELLO_DOING_LIST_ID"): Status.DOING,
    os.getenv("TRELLO_TO_DO_LIST_ID"): Status.TO_DO,
}

def get_status(list_id):
    return list_id_status[list_id]

def get_list_id(status: Status):
    return status_list_id[status]