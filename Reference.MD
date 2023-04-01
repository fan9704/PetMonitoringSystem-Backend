# Django Technical Support

## RabbitMQ

1. [Python Pika RabbitMQ 6 Implementation mode](https://www.cnblogs.com/guyuyun/p/14970592.html)
2. [Docker Compose for RabbitMQ](https://hackmd.io/@sfRJH1u7S464tSaizL7ZsQ/r1one4Rxu)
3. [Deal with Threading Conflict in Django](https://blog.csdn.net/luslin1711/article/details/87885145)

### Install Plugins for MQTT

```shell
docker exec <RabbitMQ ContainerID> rabbitmq-plugins enable rabbitmq_mqtt
docker exec <RabbitMQ ContainerID> rabbitmq-plugins enable rabbitmq_web_mqtt
docker exec <RabbitMQ ContainerID> rabbitmq-plugins enable rabbitmq_web_stomp
```

### Install RabbitMQ Management

```shell
docker exec <RabbitMQ ContainerID> rabbitmq-plugins enable rabbitmq_management
```

### Celery


Test Info
```shell
Celery -A PetMonitoringSystemBackend worker -l info
```

## Django 

1. [Django 6 Way to implement API](https://medium.com/djangotube/django-rest-api-curd-example-61c3a29b22ed)
2. [Docker Container Django](https://saadali18.medium.com/learn-docker-with-easy-implementation-in-python-django-application-82df50f351a9)
3. [Forest Admin Django](https://medium.com/forest-admin/forest-admin-django-admin-alternative-f71b3864ed65)

### Django Health Check 

1. [Django Health RabbitMQ Redis](https://ithelp.ithome.com.tw/articles/10235145)

### Django Redis

1. [Django-Redis Cache](https://ithelp.ithome.com.tw/articles/10256463)

### Django Logging

1. [Django Logstash push logging to Kibana](https://www.mls-tech.info/python/python-django-logging-to-elk/)
2. [Python Logger](https://www.cnblogs.com/jesse123/p/14135551.html)

### Django Websocket

1. [Channels Chatroom](https://zhuanlan.zhihu.com/p/373801436)

### Django Grafana Prometheus

1. [Implement Grafana Prometheus on Django](https://karanchuri.medium.com/prometheus-grafana-in-django-92da4d782f8a)

### GitHub Actions

1. [GitHub Actions Push to Docker Hub](https://blog.pradumnasaraf.dev/dockerhub-githubactions)