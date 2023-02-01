from rest_framework import serializers
from .models import *


class RegisterSerializer(serializers.ModelSerializer):
    #  = serializers.CharField(write_only=Tr  ue, required=True)
    class Meta:
        model = User
        fields = ('username','password','name')
