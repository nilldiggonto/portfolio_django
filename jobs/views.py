from django.shortcuts import render
from .models import Job
# Create your views here.

def home(request):
    queryset = Job.objects.all()

    context = {
        'jobs': queryset,
    }
    return render(request,'jobs/home.html',context)
