FROM python:3.10.5-buster
WORKDIR /code
COPY . /code
RUN pip install -r requirements.txt

CMD ["daphne", "PetMonitoringSystemBackend.asgi:application", "--bind", "0.0.0.0", "--port", "8000"]