import os
from enum import Enum

class Status(Enum):
    TO_DO = "To do"
    DOING = "Doing"
    DONE = "Done"

def get_status_from_string(status_string):
    string_to_status = {
        'To do': Status.TO_DO,
        'Doing': Status.DOING,
        'Done': Status.DONE,
    }
    return string_to_status[status_string]

def get_string_from_status(status: Status):
    status_list_id = {
        Status.DONE: 'Done',
        Status.DOING: 'Doing',
        Status.TO_DO: 'To do',
    }
    return status_list_id[status]