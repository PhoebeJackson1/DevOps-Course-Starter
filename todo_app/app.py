from flask import Flask, render_template, redirect, request
from todo_app.data.session_items import get_items, add_item
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    todo_items = get_items()
    return render_template('index.html', todo_items=todo_items)

@app.route('/add-item', methods=['POST'])
def add_ite():
    title = request.form.get('todo_title')
    add_item(title)
    return redirect("/")
