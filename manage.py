# coding: utf-8

from flask_script import Manager, Server

from app import app
from app.models import Todo

manager = Manager(app)


@manager.command
def save_todo():
    todo = Todo(content="todolist-0001")
    todo.save()


manager.add_command("runserver",
                    Server(host='0.0.0.0', port=5000, use_debugger=True)
                    )

if __name__ == "__main__":
    manager.run()
