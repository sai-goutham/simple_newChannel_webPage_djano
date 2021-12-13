from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'testapp/home.html')

def movies(request):
    return render(request,'testapp/movies.html')

def sports(request):
    return render(request,'testapp/sports.html')

def politics(request):
    return render(request,'testapp/politics.html')
