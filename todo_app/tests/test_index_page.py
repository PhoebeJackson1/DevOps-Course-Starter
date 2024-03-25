import pytest
import requests
import os
from dotenv import load_dotenv, find_dotenv
from todo_app import app

@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    test_app = app.create_app()
    with test_app.test_client() as client:
        yield client

class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    def json(self):
        return self.fake_response_data

def stub(method, url, params={}):
    test_board_id = os.environ.get('TRELLO_BOARD_ID')
    if url == f'https://api.trello.com/1/boards/{test_board_id}/cards' and method == "GET":
        fake_response_data = [
            {
                "id": "test-card-1-id",
                "idList": "test-to-do-list-id",
                "name": "Test item 1 (To do)",
            },
            {
                "id": "test-card-2-id",
                "idList": "test-doing-list-id",
                "name": "Test item 2 (Doing)",
            },
            {
                "id": "test-card-3-id",
                "idList": "test-done-list-id",
                "name": "Test item 3 (Done)",
            }
        ]
        return StubResponse(fake_response_data)

    raise Exception(f'Integration test did not expect URL "{url}"')

def check_strings_in_order(text, strings):
    remaining_text = text
    for string in strings:
        (before_text, expected_string, remaining_text) = remaining_text.partition(string)
        assert expected_string == string

def test_get_index_page(monkeypatch, client):
    monkeypatch.setattr(requests, 'request', stub)
    response = client.get('/')
    assert response.status_code == 200
    page_text = response.data.decode()
    check_strings_in_order(
        page_text, 
        ["To do tasks", "Test item 1 (To do)", "Doing tasks", "Test item 2 (Doing)", "Done tasks", "Test item 3 (Done)"]
    )
