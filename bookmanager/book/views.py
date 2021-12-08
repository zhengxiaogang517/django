from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpRequest
def index(request):
    context={
        'name':'凤非梧桐不栖'
    }
    return render(request ,'book/index.html',context=context)