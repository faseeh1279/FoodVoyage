from django.shortcuts import render 
from django.http import JsonResponse
from restaurant.models import AddFood

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


def order_now(request): 
    items = AddFood.objects.all()[:6]

    context = {"url_name":"OrderNow","items":items}
    return render(request, "ordernow.html", context)

def add_to_cart(request): 
    context = {"url_name":"AddToCart"}
    return render(request, "add_to_cart.html", context)


def get_data(request): 
    # Serialize queryset to a list of dictionaries 
    data = list(AddFood.objects.values())
    return JsonResponse(data, safe=False)


def load_items(request): 
    # Gets the current offset from the request 
    offset = int(request.GET.get('offset', 0))
    limit =6
    # Fetch the next set of items 
    items = AddFood.objects.all()[offset:offset + limit]
    # Checks if there are more items to load 
    has_more = AddFood.objects.count() > offset + limit 
    # Return the item as JSON (for AJAX call)
    return JsonResponse({
        'items':list(items.values), 
        'has_more':has_more
    })