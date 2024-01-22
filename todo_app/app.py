from flask import Flask, render_template
from todo_app.data.session_items import get_items
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    todo_items = get_items()
    return render_template('index.html', todo_items=todo_items)
