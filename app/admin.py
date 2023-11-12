from django.contrib import admin
from .models import Vhost, User, Permission, Queue, Exchange, Binding

admin.site.register([Vhost, User, Permission, Queue, Exchange, Binding])
