from django.shortcuts import render, redirect
from . import models 
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@login_required
def get_user(request): 
    return request.user 

def index(request): 
    user = get_user(request) 
    if models.Rider.objects.filter(email = user.email).exists(): 
        return redirect("/partner-with-us/rider/dashboard/")
    if request.method == "POST": 
        name = user.username 
        email = user.email
        start_time = request.POST.get("start_time")
        end_time = request.POST.get("end_time")
        city = request.POST.get("city")
        bio = request.POST.get("rider_bio")
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
    user = get_user(request)
    current_user = models.Rider.objects.get(name = user.username)
    data = models.OrderDetails.objects.filter(name = current_user)
    if data.order_status == False: 
        return redirect("deliver-order-to-customer")
    else: 
        return render(request, "rider/dashboard.html")


def rider_name(request): 
    if request.method == "GET": 
        user = get_user(request)
        data = list(models.Rider.objects.filter(user = user.username).values())
        return JsonResponse(data,safe=False )
    else: 
        return JsonResponse({"Error":"Invalid Request"})


def deliver_order(request): 
    return render(request, "rider/deliver_order.html")

@csrf_exempt
def order_details(request): 
    if request.method == "POST": 
        customer_id = request.POST.get("customer_id")
        customer_name = request.POST.get("customer_name")
        order_status = request.POST.get("order_status")
        models.OrderDetails.objects.create(
            customer_id = customer_id, 
            customer_name = customer_name, 
            order_status = order_status
        )
        return JsonResponse({"Success":"Order Details Added Successfully"})
    else: 
        return JsonResponse({"Error":"Invalid Request"})


