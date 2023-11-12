from rest_framework import serializers
from .models import Vhost, User, Permission, Queue, Exchange, Binding

class VhostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vhost
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

class QueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Queue
        fields = '__all__'

class VhostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vhost
        fields = '__all__'

class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange
        fields = '__all__'

class BindingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Binding
        fields = '__all__'

