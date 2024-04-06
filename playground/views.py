from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    name = 'Onuekwusi'
    return render(request, 'playground/index.html', {'name': name})
