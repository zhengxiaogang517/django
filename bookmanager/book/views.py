from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpRequest
def index(request):
    context={
        'name':'有朝一日权在手，杀尽天下负我狗！'
    }
    return render(request ,'book/index.html',context=context)