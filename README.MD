# Pet Monitoring Backend

![](https://img.shields.io/github/languages/top/fan9704/PetMonitoringSystem-Backend?logo=python&logoColor=%23FFFFFF&style=for-the-badge)
![](https://img.shields.io/github/languages/count/fan9704/PetMonitoringSystem-Backend?color=%23005A2B&style=for-the-badge)

## System Structure

![](./doc/SystemStructure.png)

## Software Development Lifecycle

---

[Swagger Route](127.0.0.1:8000/swagger/)

## Setup Project

### Step.1 Install Dependencies with pipenv

```shell
pipenv install
```

### Step.2 Constructor Environments with Docker-compose

```shell
docker-compose up
```

### Step.3 Environment Variables .env Setup

.env file
```dotenv
#Django
DJANGO_SECRET_KEY =
DEBUG =
#Elasticsearch
ELASTICSEARCH_ENDPOINT = 
#PostgreSQL
POSTGRES_DB =
POSTGRES_USER =
POSTGRES_PASSWORD =
POSTGRES_DB_URL =
#ChatGPT
CHATGPT_APIKEY = 
```

### Step.4 Migrate Schema to PostgreSQL

```shell
pipenv run python manage.py migrate
```

### Step.5 Migrate Index to Elasticsearch(django-elasticsearch-dsl)

```shell
pipenv run python manage.py search_index --create
```

### Step.6 Runserver

```shell
pipenv run python manage.py runserver 0.0.0.0:8000
```

----

## Other

### Install Dependencies with venv

#### Create venv

```shell
python -m venv .
```

#### Activate venv

```shell
Scripts/activate
```

#### Deactivate venv

```shell
Scripts/deactivate
```

#### Install from requirements.txt

```shell
pip install -r requirements.txt
```

#### Freeze dependencies

```shell
pip freeze > requirements.txt
```
