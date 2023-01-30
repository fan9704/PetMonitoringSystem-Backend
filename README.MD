# Pet Monitoring Backend

### Install All Dependencies with venv

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

----

### Django Elasticsearch-dsl

#### Create Index with Python

```shell
python manage.py search_index --create
```