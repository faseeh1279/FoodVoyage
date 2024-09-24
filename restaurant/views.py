from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import models 
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers
import rider.models as rider_models
import customer.models as customer_models  
import json 


# Create your views here.
@login_required
def home(request): 
    user = request.user 
    if models.Register_Partner.objects.filter(username=user.username).exists():
        return redirect('/partner-with-us/restaurant/dashboard/')
    if request.method == "POST": 
        restaurant_name = request.POST.get('restaurant_name')
        restaurant_description = request.POST.get('restaurant_description')
        restaurant_slogan = request.POST.get('restaurant_slogan')
        phone_number = request.POST.get('phone_number')
        restaurant_image = request.FILES.get('restaurant_image')
        restaurant_location = request.POST.get('restaurant_location')
        models.Register_Partner.objects.create(restaurant_name = restaurant_name, restaurant_description = restaurant_description, restaurant_slogan = restaurant_slogan, restaurant_image = restaurant_image, phone_number = phone_number, username = user.username, email = user.email, restaurant_location = restaurant_location)
        return redirect('/partner-with-us/restaurant/dashboard/')

    context = {"url_name":"Partner"}
    return render(request, "restaurant/index.html", context)

def dashboard(request): 
    return render(request, "restaurant/dashboard.html")


@login_required
def add_food(request):
    if request.method == "POST":
        restaurant = models.Register_Partner.objects.get(username=request.user.username)
        item_name = request.POST.get("item_name")
        item_description = request.POST.get("item_description")
        item_price = request.POST.get("item_price")
        item_image = request.FILES.get("item_image")

        models.AddFood.objects.create(
            restaurant=restaurant,
            item_name=item_name,
            item_description=item_description,
            item_price=item_price,
            item_image=item_image
        )
        # Redirect back to the same page after successful submission
        return redirect(request.get_full_path())

    # Fetch all food items for the logged-in restaurant
    fooditems = models.AddFood.objects.filter(restaurant__username=request.user.username)
    context = {"fooditems": fooditems}
    return render(request, "restaurant/add_food_product.html", context)
    
def update_item(request, id): 
    if request.method == "POST": 
        item_name = request.POST.get("item_name")
        item_price = request.POST.get("item_price")
        item_description = request.POST.get('item_description')
        item_image = request.FILES.get('item_image')
        models.AddFood.objects.filter(id=id).update(item_name=item_name, item_price=item_price,item_image = item_image, item_description = item_description) 
        return redirect("/partner-with-us/restaurant/dashboard/addfood/")
    context = {"url_name": "update-food-item", "id":id}
    print(id)


    return render(request, "restaurant/update_item.html", context)
 


def delete_item(request, id): 
    queryset = models.AddFood.objects.get(id = id)
    queryset.delete() 
    return redirect("/partner-with-us/restaurant/dashboard/addfood/")

@csrf_exempt
def order_details_credentails(request): 
    if request.method == "POST": 
        placed_order = customer_models.PlaceOrder.objects.filter()
        return JsonResponse(placed_order, safe=False)
    else: 
        return JsonResponse({"Error":"Invalid Request!"})


@csrf_exempt
def populate_dashboard(request):
    if request.method == "POST": 
        customer_name = request.POST.get("customer_name") 
        time_stamp = request.POST.get("time_stamp")
        customer_id = request.POST.get("customer_id")
        customer_location = request.POST.get("customer_location")
        rider_name = request.POST.get("rider_name")
        
        queryset = customer_models.PlaceOrder.objects.filter(customer_name = customer_name, users_cart = customer_id)

        for items in queryset: 
            users_cart = customer_models.Users_Cart.objects.filter(username = items.users_cart)

        rider_data = rider_models.Rider.objects.filter(name = rider_name)
        consumer_data = customer_models.ConsumerData.objects.filter(rider = rider_name, customer_name__username = customer_name, message = "OrderPlaced")
        queryset = customer_models.ConsumerData.objects.filter()
        data = {
            "queryset":list(queryset.values()), 
            "users_cart":list(users_cart.values()),
            "consumer_data":list(consumer_data.values()),
            "rider_data":list(rider_data.values())
        }
        return JsonResponse(data, safe=False)
    else: 
        return JsonResponse({"Error":"Invalid Request"})

