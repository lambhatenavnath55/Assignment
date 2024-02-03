from django.shortcuts import render
from .models import College
from .serializers import CollegeSerializer
import datetime
import random

# Create your views here.
from django.shortcuts import render

def dashboard(request):
    template_name = 'college_app/dashboard.html'
    current_time = datetime.datetime.now()
    random_quote = get_random_quote()
    context = {
        'current_time': current_time,
        'random_quote': random_quote,
    }
    return render(request, template_name, context)

def get_random_quote():
    quotes = ["Teachers can open the door, but you must enter it yourself. — Chinese proverb",
        "Education is the passport to the future, for tomorrow belongs to those who prepare for it today. — Malcolm X",
        "Education is the key to unlock the golden door of freedom."
    ]
    return random.choice(quotes)

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
