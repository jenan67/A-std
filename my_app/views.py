from django.shortcuts import render
from django.utils.text import slugify
# Create your views here.

from .models import project

def project_list(request) :
    project_list = project.objects.all()
    context = {'project_list':project_list}
    return render(request, 'project/project_list.html', context)

def project_detail(request, slug):
    project_detail = project.objects.get(Product_Slug=slug)
    context = {'project_detail' : project_detail}
    return render(request, 'project/project_detail.html' , context)

