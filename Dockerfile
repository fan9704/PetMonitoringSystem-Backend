RUN addgroup -S nonroot \
    && adduser -S nonroot -G nonroot
USER nonroot

FROM python:3.10.5-alpine
WORKDIR /code

# Folders
COPY ./PetMonitoringSystemBackend /code/PetMonitoringSystemBackend
COPY ./api /code/api
COPY ./media /code/media
# Files
COPY .env /code/.env
COPY manage.py /code/manage.py
COPY Pipfile /code/Pipfile
COPY Pipfile.lock /code/Pipfile.lock
COPY requirements.txt /code/requirements.txt
COPY prometheus.yml /code/prometheus.yml
COPY sonar-project.properties /code/sonar-project.properties

RUN pip install -r requirements.txt

CMD ["daphne", "PetMonitoringSystemBackend.asgi:application", "--bind", "0.0.0.0", "--port", "8000"]