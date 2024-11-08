import os
import pytest
from dotenv import load_dotenv, find_dotenv
from todo_app import app
import mongomock
import pymongo

@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    
    with mongomock.patch(servers=(('fakemongo.com', 27017),)):
        test_app = app.create_app()
        with test_app.test_client() as client:
            yield client

def add_mock_data_to_database():
    mock_data = [
        {
            "name": "Test item 1 (To do)",
            "status": "To do",
        },
        {
            "name": "Test item 2 (Doing)",
            "status": "Doing",
        },
        {
            "name": "Test item 3 (Done)",
            "status": "Done",
        }
    ]
    test_mongodb_client = pymongo.MongoClient(os.getenv("COSMOSDB_CONNECTION_STRING"))
    test_database = test_mongodb_client[os.getenv("DATABASE_NAME")]
    test_collection = test_database[os.getenv("ITEMS_COLLECTION_NAME")]
    test_collection.insert_many(mock_data)

def check_strings_in_order(text, strings):
    remaining_text = text
    for string in strings:
        (before_text, expected_string, remaining_text) = remaining_text.partition(string)
        assert expected_string == string

def test_get_index_page(client):
    add_mock_data_to_database()
    response = client.get('/')
    assert response.status_code == 200
    page_text = response.data.decode()
    check_strings_in_order(
        page_text, 
        ["To do tasks", "Test item 1 (To do)", "Doing tasks", "Test item 2 (Doing)", "Done tasks", "Test item 3 (Done)"]
    )
