from todo_app.data.status import Status
from todo_app.data.item import Item

class ViewModel:
    def __init__(self, items):
        self._items = items
 
    @property
    def items(self):
        return self._items
    
    @property
    def to_do_items(self):
        return [item for item in self.items if item.status == Status.TO_DO]
    
    @property
    def doing_items(self):
        return [item for item in self.items if item.status == Status.DOING]
    
    @property
    def done_items(self):
        return [item for item in self.items if item.status == Status.DONE]