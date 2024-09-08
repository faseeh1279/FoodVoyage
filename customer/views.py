from django.shortcuts import render, HttpResponse
from restaurant.models import AddFood
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from . import models 
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    user = request.user 
    if models.Users_Cart.objects.filter(username = user.username).exists(): 
        items = AddFood.objects.all() 
        context = {"url_name":"Home", "queryset":items}
        return render(request, "customer/index.html",context)
    else: 
        models.Users_Cart.objects.create(username = user.username, email = user.email)
        items = AddFood.objects.all() 
        context = {"url_name":"Home", "queryset":items}
        return render(request, 'customer/index.html', context)


@login_required
@csrf_exempt
def add_to_cart(request): 
    user = request.user 
    if models.AddToCart.objects.filter(username = user.username).exists(): 
        if request.method == 'POST':
            itemId = request.POST.get('itemId')
            queryset = AddFood.objects.get(id = itemId)
            cart_queryset =  models.AddToCart.objects.filter(username = user.username).all()  
            
            return JsonResponse({"Message":"Successfully Added Data"})
        else: 
            return JsonResponse({"Message":"Invalid Request"})
    pass 
        

def notification(request): 
    context = {
        "url_name":"notification"
    }
    return render(request, "notification.html", context)

def order_now(request): 
    items = AddFood.objects.all()
    context = {"url_name":"OrderNow","queryset":items}
    return render(request, "customer/ordernow.html", context)



