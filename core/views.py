from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.core.paginator import Paginator
from restaurant.models import * 
import json 
from customer.models import *
from django.contrib.auth.decorators import login_required
# Define your views here 


def about_page(request): 
    context = {"url_name":"About"}
    return render(request, "about.html",context)

def services_page(request): 
    context = {"url_name":"Services"}
    return render(request, "services.html", context)

def contact_us(request): 
    context = {"url_name":"Contact"}
    return render(request, "contact.html", context)

@login_required
def get_user(request): 
    return request.user 

def cart(request): 
    if request.method == "GET": 
        user = get_user(request)
        users_cart = Users_Cart.objects.get(username=user.username)
        data = list(AddToCart.objects.filter(users_cart=users_cart).values())
        return JsonResponse(data, safe=False)
    else: 
        return JsonResponse({"Error":"Invalid Request"})








def notification(request): 
    context = {
        "url_name":"notification"
    }
    return render(request, "notification.html", context)