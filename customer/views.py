from django.shortcuts import render, HttpResponse
from restaurant.models import AddFood
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import models 
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    user = request.user 
    if models.Users_Cart.objects.filter(username=user.username).exists(): 
        items = AddFood.objects.all() 
        context = {"url_name":"Home", "queryset":items}
        return render(request, "customer/index.html", context)
    else: 
        models.Users_Cart.objects.create(username=user.username, email=user.email)
        items = AddFood.objects.all() 
        context = {"url_name":"Home", "queryset":items}
        return render(request, 'customer/index.html', context)

@login_required
def get_user(request): 
    return request.user
 
@csrf_exempt
def add_to_cart(request): 
    user = get_user(request)  
    if request.method == 'POST':
        itemId = request.POST.get('itemId')
        users_cart = models.Users_Cart.objects.get(username=user.username)
        queryset = AddFood.objects.get(id=itemId)
        models.AddToCart.objects.create(
            users_cart=users_cart, 
            item_name=queryset.item_name, 
            item_image=queryset.item_image, 
            item_price=queryset.item_price
        )
        return JsonResponse({"Message": "Successfully Added Data"})
    else: 
        return JsonResponse({"Message": "Invalid Request"})

def notification(request): 
    context = {"url_name": "notification"}
    return render(request, "notification.html", context)

def order_now(request): 
    items = AddFood.objects.all()
    context = {"url_name": "OrderNow", "queryset": items}
    return render(request, "customer/ordernow.html", context)


def view_cart(request): 
    context = {"url_name":"AddToCart"}
    return render(request, "customer/view_cart.html", context)

def get_data(request): 
    user = request.user  # Using the authenticated user object
    if request.method == "GET": 
        users_cart = models.Users_Cart.objects.get(username=user.username)
        data = models.AddToCart.objects.filter(users_cart=users_cart).values()  # Use `values()` to return a list of dictionaries
        return JsonResponse(list(data), safe=False)  # Convert QuerySet to a list for JSON response
    else: 
        return JsonResponse({"Error":"Invalid Request"})
    
@csrf_exempt
def delete_data(request): 
    if request.method == "POST": 
        itemId = request.POST.get("itemId")
        data = list(models.AddToCart.objects.filter(id = itemId).values())
        models.AddToCart.objects.filter(id= itemId).delete()  
        return JsonResponse(data, safe=False)
    else: 
        return JsonResponse({"Error":"Invalid Request"})


def get_cart_details(request): 
    if request.method == "GET": 
        user = get_user(request) 
        users_cart = models.Users_Cart.objects.get(username = user.username)
        data = models.AddToCart.objects.filter(users_cart = users_cart).values() 
        return JsonResponse(list(data), safe=False)
    else: 
        return JsonResponse({"Error":"Invalid Request"})