from django.shortcuts import render, redirect
from . import models 
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def get_user(request): 
    return request.user 

def index(request): 
    user = get_user(request) 
    if models.Rider.objects.filter(email = user.email).exists(): 
        return redirect("/partner-with-us/rider/dashboard/")
    if request.method == "POST": 
        name = request.POST.get("rider_name")
        start_time = request.POST.get("start_time")
        end_time = request.POST.get("end_time")
        city = request.POST.get("city")
        bio = request.POST.get("rider_bio")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        profile_image = request.POST.get("profile_image")
        vehicle_type = request.POST.get("vehicle_type")
        models.Rider.objects.create(
            name = name,
            email = email, 
            start_time = start_time, 
            end_time = end_time, 
            city = city, 
            bio = bio, 
            phone_number = phone_number, 
            profile_image = profile_image, 
            vehicle_type = vehicle_type
        )
        return render(request, 'rider/index.html')


    return render(request,"rider/index.html")

def dashboard(request): 
    return render(request, "rider/dashboard.html")

