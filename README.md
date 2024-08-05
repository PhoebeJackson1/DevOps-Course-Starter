# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.8+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

You can check poetry is installed by running `poetry --version` from a terminal.

**Please note that after installing poetry you may need to restart VSCode and any terminals you are running before poetry will be recognised.**

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/2.3.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

Set up a Trello Account (https://trello.com/signup) and create an API Key and an API Token for Trello and then put the values in your .env file and the relevant trello board ids for your set up.

## Running the App
### Locally

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app 'todo_app/app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 113-666-066
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

### Remotely using Ansible

There is an ansible playbook found in `ansible/` to run the app from remote hosts. To use it run:
```bash
 ansible-playbook ansible-playbook.yml -i ansible-inventory.ini
```
(from `/ansible` directory on a control node).

If adding a new remote host add it's public IP to `ansible/ansible-inventory.ini`.
 
Now visit `<host-IP-address>:5000/` in your web browser to view the app.

### Using Docker

Build and run a development container (with hot reloading) using:
```bash
docker build --target development --tag todo-app:dev .
docker run --env-file .env -p 5100:5000 --mount "type=bind,source=$(pwd)/todo_app,target=/code/todo_app" todo-app:dev
```
The app will then be accessible at [`http://localhost:5100/`](http://localhost:5100/).

Or for the production version use: 
```bash
docker build --target production --tag todo-app:prod .
docker run --env-file .env -p 5100:5000 todo-app:prod
```
(NB: If your .env file contains a value for FLASK_DEBUG that needs to be set to false for production)

### Hosting on Azure

The todo-app is available at https://phojac-todo-app.azurewebsites.net/

Push the latest docker image to the [DockerHub repository](https://hub.docker.com/repository/docker/phoebejackson/todo-app/general) using:

```bash
docker build --target production --tag phoebejackson todo-app:prod .
docker push  phoebejackson/todo-app:prod
```

Send a POST request to the webhook URL (which can be found in Deployment Centre on Azure Portal) to prompt Azure to pull the updated image from DockerHub.

## Running the tests for the App

### Locally

There are some tests for the app that are found in `todo_app/tests`. They can be run using the command:
```bash 
$ poetry run pytest
```
To run only tests in a particular test file use:
```bash 
$ poetry run pytest <relative file path>
```
Or for a single test use:
```bash 
$ poetry run pytest <relative file path>::<test name>
```

### Using Docker

To run the tests in Docker use: 
```bash
docker build --target test --tag todo-app:test .
docker run --env-file .env.test todo-app:test
```

### CI

The tests are also run by GitHub Actions on push and pull request events.


