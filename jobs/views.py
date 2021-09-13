from django.shortcuts import render, get_object_or_404
from .models import Job

def homepage(request):
    jobs = Job.objects
    return render(request, 'home.html',{'jobs':jobs})

def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk = job_id)#pk -> primary key in the db
    return render(request, 'detail.html', {'job':job_detail})