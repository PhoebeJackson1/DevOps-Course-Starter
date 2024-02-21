from flask import Flask, render_template, redirect, request
from todo_app.data.trello_items import get_items_from_trello, add_item_to_trello, change_status_of_item_on_trello, Status
from todo_app.flask_config import Config
import os

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    todo_items = get_items_from_trello()
    return render_template('index.html', todo_items=todo_items)

@app.route('/add-item', methods=['POST'])
def add_item():
    title = request.form.get('todo_title')
    add_item_to_trello(title)
    return redirect("/")

@app.route('/item-done', methods=['POST'])
def item_done():
    id = request.form.get('id')
    print(id)
    change_status_of_item_on_trello(id, Status.DONE)
    return redirect("/")

@app.route('/item-doing', methods=['POST'])
def item_doing():
    id = request.form.get('id')
    print(id)
    change_status_of_item_on_trello(id, Status.DOING)
    return redirect("/")

@app.route('/item-to-do', methods=['POST'])
def item_to_do():
    id = request.form.get('id')
    print(id)
    change_status_of_item_on_trello(id, Status.TO_DO)
    return redirect("/")