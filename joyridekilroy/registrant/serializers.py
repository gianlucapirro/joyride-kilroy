from rest_framework import serializers
from .models import Registrant
from django.core.validators import RegexValidator
from rest_framework.validators import UniqueValidator

phone_regex = "^[\+][0-9]{10,15}$"
phone_validator = RegexValidator(
    regex=phone_regex,
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
)

class RegistrantSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(validators=[phone_validator, UniqueValidator(queryset=Registrant.objects.all())])
    
    class Meta:
        model = Registrant
        fields = "__all__"
