from django import forms
from .models import RabbitMQInfo

class RabbitMQInfoForm(forms.ModelForm):
    class Meta:
        model = RabbitMQInfo
        fields = ['version', 'cluster_name']
