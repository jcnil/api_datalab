# CHALLENGE DATA LAB

## About The Project

Microservice in charged to sign and verify documents with CHALLENGE DATA LAB services

### Built With
* Language: Python 3.9.15
* Framework: FastApi
* ODM: mongoengine

```
api_datalab/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── serializer.py
│   │       └── views.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── constants.py
│   │   ├── enums.py
│   │   ├── exceptions.py
│   │   ├── handlers.py
│   │   ├── helpers.py
│   │   ├── models.py
│   │   ├── process.py
│   │   └── querysets.py
│   │
│   └── meta/
│       ├── __init__.py
│       └── views.py
│
├── config/
│   ├── __init__.py
│   ├── db.py
│   └── urls.py
│
├── README.md
└── requirements.txt
└── .env.example
```

## Getting Started

This is an example of how you may follow instructions on setting up your project locally. To get a local copy up and running follow these simple example steps.

### Prerequisites
* [MongoDB Installation](https://docs.mongodb.com/manual/installation/)

Once you have MongoDB installed, and if you are going to run the project on local, please check that mongo
is running in your pc with the next command, or maybe you should validate if you have installed docker and mongo dockerized:

```sh
sudo systemctl status mongod
```

### Installation 

1. Install the virtual environment
```sh
$ python3 -m venv venv
```
Activate the virtual environment with:
```sh
$ source venv/bin/activate
```
2. Install project requirements
```sh
$ pip3 install -r requirements.txt
```

Configuration
=============

## Set environment variables of config

Env vars of project configuration:

ENV VAR                         |   DESCRIPTION                                     |
---                             |   ---                                             |
APP_ENV                         |   local, staging, production                      |
MONGO_URI                       |   Mongo URI                                       |

### Execution

### run Server
```sh
$ uvicorn config:app --host=0.0.0.0 --port=8001 --reload --log-level=info
```

Develop
=======

## Run Flake8

```sh
flake8 --exclude venv/ --max-line-length 120
```

or 

```sh
python -m flake8 --exclude venv/ --max-line-length 120
```

Contact
=======
[Jose Nicolielly](https://github.com/jcnil/api_datalab)
```
