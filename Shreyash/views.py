from django.shortcuts import render

def loading(request):
    return render(request, 'loading.html')

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def project(request):
    return render(request, 'project.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')
