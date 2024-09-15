from django.shortcuts import render, redirect
from . import models 
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import customer.models as customer_models  
import restaurant.models as restaurant_models 
import json 

# Create your views here.


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

def dashboard(request): 
    user = get_user(request)
    # Get the current rider object
    try:
        current_user = models.Rider.objects.get(name=user.username)
        
    except models.Rider.DoesNotExist:
        
        return redirect("/some-error-page/")  # Redirect or handle the case when rider is not found

    # Filter all pending orders for the current rider
    pending_orders = models.OrderDetails.objects.filter(rider=current_user, order_status=False)
    
    if pending_orders.exists(): 
        
        # If there's at least one pending order, you can redirect to the delivery page
        return redirect("/partner-with-us/rider/deliver-order-to-customer/")
    else:
        
        rider_dashboard_dictionary = [] 
        rider_dashboard_data = customer_models.ConsumerData.objects.all()
        for item in rider_dashboard_data: 
            rider_dashboard_dictionary.append(
                {
                'customer_name': item.customer_name.username,  
                'message': item.message,
                'time_stamp': item.time_stamp,
                'customer_id': item.customer_id,
                'customer_location': item.customer_location,
                'rider': item.rider,
                }
            )
        context = {
            "url_name":"Dashboard",
            "rider_dashboard_data":rider_dashboard_dictionary
        }
        return render(request, "rider/dashboard.html", context)


def rider_name(request): 
    if request.method == "GET": 
        user = get_user(request)
        print(user.username)
        current_rider_name = models.Rider.objects.get(name = user.username)
        print("Object Caught successfully", current_rider_name.name) 
        data = current_rider_name.name 
        return JsonResponse(data, safe=False)

    else: 
        return JsonResponse({"Error":"Invalid Request"})


def deliver_order(request): 
    
    return render(request, "rider/deliver_order.html")

@csrf_exempt
def order_details(request): 
    user = get_user(request) 
    if request.method == "POST": 
        

        customer_id = request.POST.get("customer_id")
        customer_name = request.POST.get("customer_name")
        order_status = request.POST.get("order_status")
        rider_name = request.POST.get("rider_name") 
        time_stamp = request.POST.get("time_stamp")
        message = request.POST.get("message")
        location = request.POST.get("location")
        
        
        
        try:
            current_user = models.Rider.objects.get(name=user.username)
        except models.Rider.DoesNotExist:
            return JsonResponse({"Error": "Rider not found"}, status=404)
        
        models.OrderDetails.objects.create(
            rider=current_user,  
            customer_id=customer_id, 
            customer_name=customer_name, 
            order_status=order_status,
            rider_name=rider_name 
        )
        data = customer_models.ConsumerData.objects.filter(customer_id = customer_id)
        for items in data:
            items.message = message
            items.customer_location = location 
            items.time_stamp = time_stamp
            items.save() 
        return JsonResponse({"Success": "Order Details Added Successfully"})
    else: 
        return JsonResponse({"Error": "Invalid Request"})

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
    

def check_placed_orders(request): 
    if request.method == "GET": 
        consumerdata = customer_models.ConsumerData.objects.filter(message = "PlaceOrder")
        data = [] 
        for items in consumerdata: 
            data.append({
                "customer_id":items.customer_id,
                "customer_name":items.customer_name.username,
                "message":items.message, 
                "time_stamp":items.time_stamp, 
                "customer_location":items.customer_location, 
                "rider":items.rider 
            })
        
        return JsonResponse(data, safe=False)
    else: 
        return JsonResponse({"Error":"Invalid Request"})
    

def get_placed_orders_details(request): 
    if request.method == "GET":
        user = get_user(request)
        rider_name = models.Rider.objects.get(name = user.username)
        data = list(customer_models.ConsumerData.objects.filter(rider = rider_name).values())
        return JsonResponse(data, safe=False)
    else: 
        return JsonResponse({"Error":"Invalid Request"})
    




    

