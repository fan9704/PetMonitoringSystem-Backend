# Django Technical Support

## RabbitMQ

1. [Python Pika RabbitMQ 6 Implementation mode](https://www.cnblogs.com/guyuyun/p/14970592.html)
2. [Docker Compose for RabbitMQ](https://hackmd.io/@sfRJH1u7S464tSaizL7ZsQ/r1one4Rxu)
3. [Deal with Threading Conflict in Django](https://blog.csdn.net/luslin1711/article/details/87885145)

### Install Plugins for MQTT

```shell
docker exec -it <RabbitMQ ContainerID Or Container Name> rabbitmq-plugins enable rabbitmq_mqtt
docker exec -it <RabbitMQ ContainerID Or Container Name> rabbitmq-plugins enable rabbitmq_web_mqtt
docker exec -it <RabbitMQ ContainerID Or Container Name> rabbitmq-plugins enable rabbitmq_web_stomp
```

### Install RabbitMQ Management

```shell
docker exec <RabbitMQ ContainerID Or Container Name> rabbitmq-plugins enable rabbitmq_management
```

### Check RabbitMQ current plugins

```shell
docker exec <RabbitMQ ContainerID Or Container Name> rabbitmq-plugins list
```

### Celery


Test Info
```shell
Celery -A PetMonitoringSystemBackend worker -l info
```

----

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
3. [Python Logging Handler](https://blog.csdn.net/yypsober/article/details/51800120)
4. [Python Logger Produce Log File](https://shian420.pixnet.net/blog/post/350291572-%5Bpython%5D-logging-%E5%B9%AB%E4%BD%A0%E7%B4%80%E9%8C%84%E4%BB%BB%E4%BD%95%E8%A8%8A%E6%81%AF)

### Django Websocket

1. [Channels Chatroom](https://zhuanlan.zhihu.com/p/373801436)
2. [Django Websockets: A Complete Beginners Guide!](https://esketchers.com/django-websockets-a-complete-beginners-guide/)

### Django Grafana Prometheus

1. [Implement Grafana Prometheus on Django](https://karanchuri.medium.com/prometheus-grafana-in-django-92da4d782f8a)

### Django Migration and Seed

1. [Seeding and Migration through Django-Seed](https://medium.com/@ardho/migration-and-seeding-in-django-3ae322952111)

### GitHub Actions

1. [GitHub Actions Push to Docker Hub](https://blog.pradumnasaraf.dev/dockerhub-githubactions)

### Daphne

1. [Daphne Django Static file missing](https://blog.csdn.net/zy010101/article/details/121679187)
2. [Django Deploy through Daphne](https://wyde.github.io/2017/11/24/Deploying-Django-Channels-using-Daphne/)


### Ubuntu

1. [Install Python3 in Ubuntu](https://computingforgeeks.com/how-to-install-python-on-ubuntu-linux-system/)

### Sonar Qube

1. [Fix Container Hosting maximum memory problem](https://blog.csdn.net/weixin_39643007/article/details/108435139)

### Firebase

Note: FCM V1 not support post request directly should pass OAuth 2.0 Authentication

1. [FCM V1 through OAuth 2.0](https://apoorv487.medium.com/testing-fcm-push-notification-http-v1-through-oauth-2-0-playground-postman-terminal-part-2-7d7a6a0e2fa0)