from todo_app.data.status import Status, get_status

class Item:
    def __init__(self, id, name, status: Status = Status.TO_DO):
        self.id = id
        self.name = name
        self.status = status

    @classmethod
    def from_trello_card(cls, card):
        return cls(card['id'], card['name'], get_status(card['idList'])) 
