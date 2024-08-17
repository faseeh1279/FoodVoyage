from django.shortcuts import render

# Create your views here.
def home(request): 
    context = {"url_name":"Partner"}
    return render(request, "restaurant/index.html")

def dashboard(request): 
    return render(request, "restaurant/dashboard.html")