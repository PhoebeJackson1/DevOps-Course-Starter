import os
from enum import Enum

to_do_list_id = os.getenv("TRELLO_TO_DO_LIST_ID")
doing_list_id = os.getenv("TRELLO_DOING_LIST_ID")
done_list_id = os.getenv("TRELLO_DONE_LIST_ID")

class Status(Enum):
    TO_DO = "To do"
    DOING = "Doing"
    DONE = "Done"

status_list_id = {
    Status.DONE: done_list_id,
    Status.DOING: doing_list_id,
    Status.TO_DO: to_do_list_id,
}

list_id_status = {
    done_list_id: Status.DONE,
    doing_list_id: Status.DOING,
    to_do_list_id: Status.TO_DO,
}

def get_status(list_id):
    return list_id_status[list_id]

def get_list_id(status: Status):
    return status_list_id[status]