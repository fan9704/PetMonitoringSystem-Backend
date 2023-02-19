FROM python:3.9-buster
WORKDIR /code
COPY . /code
RUN pip install -r requirements.txt
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]