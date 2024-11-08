from todo_app.data.status import Status, get_status_from_string

class Item:
    def __init__(self, id, name, status: Status = Status.TO_DO):
        self.id = id
        self.name = name
        self.status = status

    @classmethod
    def from_database_item(cls, item):
        return cls(item["_id"], item["name"], get_status_from_string(item["status"]))