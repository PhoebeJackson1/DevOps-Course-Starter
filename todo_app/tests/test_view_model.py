from todo_app.data.status import Status
from todo_app.data.item import Item
from todo_app.data.view_model import ViewModel

def test_view_model_done_items():
    test_to_do_item = Item("test-id-1", "Test item with status to do", Status.TO_DO)
    test_done_item = Item("test-id-2", "Test item with status done", Status.DONE)
    test_items = [test_done_item, test_to_do_item]
    view_model = ViewModel(test_items)
    done_items = view_model.done_items
    assert test_done_item in done_items
    assert test_to_do_item not in done_items