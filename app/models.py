from django.db import models

class RabbitMQInfo(models.Model):
    version = models.CharField(max_length=50)
    cluster_name = models.CharField(max_length=100)

class Vhost(models.Model):
    name = models.CharField(max_length=100, unique=True)

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

class Permission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vhost = models.ForeignKey(Vhost, on_delete=models.CASCADE)
    configure = models.CharField(max_length=50, default='.*')
    write = models.CharField(max_length=50, default='.*')
    read = models.CharField(max_length=50, default='.*')

class Queue(models.Model):
    name = models.CharField(max_length=100)
    vhost = models.ForeignKey(Vhost, on_delete=models.CASCADE)

class Exchange(models.Model):
    name = models.CharField(max_length=100)
    vhost = models.ForeignKey(Vhost, on_delete=models.CASCADE)

class Binding(models.Model):
    source = models.ForeignKey(Exchange, on_delete=models.CASCADE, related_name='source_bindings')
    destination = models.ForeignKey(Exchange, on_delete=models.CASCADE, related_name='destination_bindings')
    destination_type = models.CharField(max_length=100)
    routing_key = models.CharField(max_length=100)

