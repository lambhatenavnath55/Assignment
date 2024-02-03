from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def dashboard(request):
    template_name = 'college_app/dashboard.html'
    return render(request, template_name)
