from rest_framework import serializers
from .models import user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields=["first_name","last_name","age","email","phone"]


    def validate_age(self, age):
        if not (0 <= age <= 120):
            raise serializers.ValidationError("Age must be between 0 and 120.")
        return age
    
    def validate_first_name(self, first_name):
        if not first_name.strip():
            raise serializers.ValidationError("first name  cannot be empty.")
        return first_name
    
    def validate_last_name(self, last_name):
        if not last_name.strip():
            raise serializers.ValidationError("last name  cannot be empty.")
        return last_name