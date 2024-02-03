from rest_framework import serializers
from .models import College, Professor, Department

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ['id', 'name', 'location', 'established', 'description', 'website', 'contact_email']

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['first_name', 'last_name', 'department', 'email']
        
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name', 'college']