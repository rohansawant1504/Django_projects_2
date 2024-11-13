from rest_framework import serializers
from .models import employee_data

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee_data
        fields = "__all__"
