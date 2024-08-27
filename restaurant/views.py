from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import models 
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers


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
        models.Register_Partner.objects.create(restaurant_name = restaurant_name, restaurant_description = restaurant_description, restaurant_slogan = restaurant_slogan, restaurant_image = restaurant_image, phone_number = phone_number, username = user.username, email = user.email)
        return redirect('/partner-with-us/restaurant/dashboard/')

    context = {"url_name":"Partner"}
    return render(request, "restaurant/index.html")

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