from django.shortcuts import render, redirect
from . import models 
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import customer.models as customer_models  
import restaurant.models as restaurant_models 
import json 



# Index Views 
@login_required
def get_user(request): 
    return request.user 

def index(request): 
    user = get_user(request) 
    if models.Rider.objects.filter(email = user.email).exists(): 
        return redirect("/partner-with-us/rider/dashboard/")
    elif request.method == "POST": 
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
    else: 
        return render(request,"rider/index.html")



def deliver_order(request): 
    rider = get_user(request)
    


    context = {
        "url_name":"DeliverOrder", 
        }
    return render(request, "rider/deliver_order.html", context)

@csrf_exempt
def get_order_details(request): 
    if request.method == "POST": 
        customer_name = request.POST.get("customer_name")
        customer_id = request.POST.get("customer_id")
        restaurant_name = request.POST.get("restaurant_name")
        place_order_data = list(customer_models.PlaceOrder.objects.filter(customer_name = customer_name, users_cart_id = customer_id ).values())
        restaurant_location = restaurant_models.Register_Partner.objects.get(restaurant_name = restaurant_name) 

        data = {
            "place_order_data":place_order_data, 
            "restaurant_location":restaurant_location
        }
        
        return JsonResponse(data, safe=False)
    else: 
        return JsonResponse({"Error":"Invalid Request"})

    


def dashboard(request): 
    user = get_user(request)
    queryset = models.Rider.objects.get(name = user.username)
    context = {
        "url_name":"Dashboard", 
        "queryset":queryset.name
    }
     
    return render(request, "rider/dashboard.html", context)

@csrf_exempt
def get_customer_phoneNumber(request): 
    if request.method == "POST": 
        customer_name = request.POST.get("customer_name")
        queryset = customer_models.Users_Cart.objects.get(username=customer_name)
        customer_phoneNumber = queryset.phone_number  
        return JsonResponse(customer_phoneNumber, safe=False)
    else: 
        return JsonResponse({"Message":"Invalid Request"})
    

def get_orders(request): 
    if request.method == "GET":
        data = list(customer_models.ConsumerData.objects.filter(message = "OrderPlaced").values())
        queryset =list(customer_models.Users_Cart.objects.all().values())
        dictionary = {
            "consumer_data":data,
            "users_cart":queryset
        }
        return JsonResponse(json.dumps(dictionary), safe=False)
    else: 
        return JsonResponse({"Error":"Invalid Request"})
    

def get_rider_name(request): 
    if request.method == "GET":
        user = get_user(request)
        rider_name = models.Rider.objects.get(name = user.username)
        return JsonResponse(rider_name.name, safe=False)
    else: 
        return JsonResponse({"Error":"Invalid Request"})
    


@csrf_exempt
def upload_consumer_data(request):
    if request.method == "POST":
        rider = request.POST.get("rider")
        customer_id = request.POST.get("customer_id")
        queryset = customer_models.ConsumerData.objects.filter(customer_id = customer_id)
        for items in queryset: 
            items.rider = rider
            items.save() 
        return JsonResponse({"Message":"Data Saved Successfully"})
    else: 
        return JsonResponse({"Message":"Invalid Request"})




        






    




    

