from rest_framework import serializers
from createresume.models import *

class PersonalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalDetails
        fields = ['id', 'name', 'parents_name', 'gender']