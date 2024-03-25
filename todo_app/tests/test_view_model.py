from todo_app.data.status import Status
from todo_app.data.item import Item
from todo_app.data.view_model import ViewModel

test_to_do_item = Item("test-id-to-do-1", "Test item with status to do", Status.TO_DO)
test_doing_item = Item("test-id-doing-1", "Test item with status doing", Status.DOING)
test_done_item = Item("test-id-done-1", "Test item with status done", Status.DONE)
test_items = [test_to_do_item, test_doing_item, test_done_item]
view_model = ViewModel(test_items)


def test_view_model_to_do_items():
    to_do_items = view_model.to_do_items
    assert test_to_do_item in to_do_items
    assert test_doing_item not in to_do_items
    assert test_done_item not in to_do_items
    assert len(to_do_items) == 1

def test_view_model_doing_items():
    doing_items = view_model.doing_items
    assert test_doing_item in doing_items
    assert test_to_do_item not in doing_items
    assert test_done_item not in doing_items
    assert len(doing_items) == 1


def test_view_model_done_items():
    done_items = view_model.done_items
    assert test_done_item in done_items
    assert test_doing_item not in done_items
    assert test_to_do_item not in done_items
    assert len(done_items) == 1
