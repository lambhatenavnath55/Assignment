from django.shortcuts import render
from .models import College
from .serializers import CollegeSerializer

# Create your views here.
from django.shortcuts import render

def dashboard(request):
    template_name = 'college_app/dashboard.html'
    return render(request, template_name)

def home(request):
    template_name = 'college_app/home.html'
    clg_info = College.objects.all()
    serializer =  CollegeSerializer(clg_info, many=True)
    return render(request, template_name, {'serialized_data': serializer.data})

def about(request):
    template_name = 'college_app/about.html'
    college_object = College.objects.first()
    return render(request, template_name, {'description': college_object.description})

def contact(request):
    template_name = 'college_app/contact.html'
    college_object = College.objects.first()
    return render(request, template_name, {'contact':college_object.contact_email})
