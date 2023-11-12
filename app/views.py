from rest_framework import viewsets
from django.http import HttpResponse
from django.shortcuts import render
from .models import Vhost, User, Permission, Queue, Exchange, Binding, RabbitMQInfo
from .serializers import VhostSerializer, UserSerializer, PermissionSerializer, QueueSerializer, ExchangeSerializer, BindingSerializer
from .forms import RabbitMQInfoForm

import json

def schema_generator(request):
    # Manejar el formulario para la información de RabbitMQ
    if request.method == 'POST':
        form = RabbitMQInfoForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = RabbitMQInfoForm()

    # Obtener los datos de los modelos para el esquema
    data = {
        # Obtener la información de RabbitMQ
        "rabbit_version": form.instance.version if form.instance else "3.12.6",
        "global_parameters": [{
            "name": "cluster_name",
            "value": form.instance.cluster_name if form.instance else "rabbit@node"
        }],
        # Obtener los datos de los modelos
        "vhosts": list(Vhost.objects.all().values()),
        "users": list(User.objects.all().values()),
        "permissions": list(Permission.objects.all().values()),
        "queues": list(Queue.objects.all().values()),
        "exchanges": list(Exchange.objects.all().values()),
        "bindings": list(Binding.objects.all().values()),
    }

    if request.method == 'POST' and form.is_valid():
        file_content = json.dumps(data, indent=4)
        response = HttpResponse(file_content, content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="schema.definitions.json"'
        return response

    return render(request, 'generator.html', {'form': form})

class VhostViewSet(viewsets.ModelViewSet):
    queryset = Vhost.objects.all()
    serializer_class = VhostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class QueueViewSet(viewsets.ModelViewSet):
    queryset = Queue.objects.all()
    serializer_class = QueueSerializer

class ExchangeViewSet(viewsets.ModelViewSet):
    queryset = Exchange.objects.all()
    serializer_class = ExchangeSerializer

class BindingViewSet(viewsets.ModelViewSet):
    queryset = Binding.objects.all()
    serializer_class = BindingSerializer