from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response
import csv

from users.models import user
from users.serializers import UserSerializer


class FileUploadViewset(ViewSet):
    def create(self,request,*args, **kwargs):

        file = request.FILES['file']
        
        if not file.name.endswith('.csv'):
            return Response({"message": "Only .csv files are accepted."})

        valid_records = 0
        rejected_records = 0
        validation_errors = []

        reader = csv.DictReader(file.read().decode('utf-8').splitlines())
        
        for row in reader:
            first_name = row.get('first_name')
            last_name  =row.get('last_name')
            email = row.get('email')
            age = row.get('age')
            phone = row.get('phone')

            if not first_name or not email or not age or not last_name or not phone:
                rejected_records += 1
                validation_errors.append("Missing fields in row.")
                continue

            user_data = {'first_name': first_name,'last_name': last_name,'phone':phone, 'email': email, 'age': int(age)}
            if not user.objects.filter(email=email).exists():
                valid_records += 1
            else:
                rejected_records += 1
                validation_errors.append(f"Duplicate email: {email}")


            serializer = UserSerializer(data=user_data)
            if serializer.is_valid():
                    serializer.save()
               
            else:
                rejected_records += 1
                validation_errors.append(serializer.errors)

        response_data = {
            'valid_records': valid_records,
            'rejected_records': rejected_records,
            'validation_errors': validation_errors
        }
        return Response({"data":response_data})