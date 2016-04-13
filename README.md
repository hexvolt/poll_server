POLL SERVER
===========

This is a test application that implements a REST API for managing polls and
customer votes. It provides a RESTful access to the Questions and Choices
instances, following logic of Django's tutorial application.


Setting up and Installation
---------------------------
* Clone the project



    git clone git@bitbucket.org:hexvolt/poll_server.git

* Set up your environment

This project is intended to work with Python 3+, however it may support
Python 2.7 as well. If you are going to work with Python 3 (preferable) - it is
recommended to install Python3.5 first and create its virtual environment in
your virtualenv folder:

    pyvenv-3.5 <env_name>
    cd <env_name>
    source bin/activate

* Set up RabbitMQ

Install a RabbitMQ server and set up its users and permissions if you
didn't do that before:


    rabbitmqctl add_user <username> <password>
    sudo rabbitmqctl set_permissions guest ".*" ".*" ".*"

Write down the parameters you've' just used for configuration into your
environment variables or to the setting.py file (see RABBITMQ_USER,
RABBITMQ_PASSWORD, etc)

* Finally install the requirements and run the project

After activating your virtualenv, go to the folder with cloned project and run:


    pip install -r requirements.txt
    python manage.py migrate
    make run

Usage
-----

To enter application's admin dashboard, create a django superuser and go to
[http://0.0.0.0:8000/admin/](http://0.0.0.0:8000/admin/) page.

You can see browsable API by visiting [http://0.0.0.0:8000/](http://0.0.0.0:8000/)

To make a vote on certain question/choice - use:

    POST http://0.0.0.0:8000/questions/<question_id>/vote
    {"choice": <choice_id>}
