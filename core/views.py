from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.core.paginator import Paginator
from restaurant.models import AddFood
import json 
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

    context = {"url_name":"OrderNow","queryset":items}
    return render(request, "ordernow.html", context)

def view_cart(request): 
    context = {"url_name":"AddToCart"}
    return render(request, "add_to_cart.html", context)


def get_data(request): 
    # Serialize queryset to a list of dictionaries 
    data = list(AddFood.objects.values())
    return JsonResponse(data, safe=False)


def load_more_posts(request):

    page_number = request.GET.get('page')
    posts = AddFood.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 6)  # Show 6 items per page

    try:
        page_obj = paginator.page(page_number)
    except:
        page_obj = paginator.page(1)

    posts_data = list(page_obj.object_list.values('item_name', 'item_price', 'item_image'))

    return JsonResponse({
        'posts': posts_data,
        'has_next': page_obj.has_next(),
    })


def add_to_card(request, item_id): 
    item = get_object_or_404(AddFood, id = item_id)
    # Get existing cart data from cookies 
    cart = request.COOKIES.get('cart')  
    if cart: 
        cart = json.loads(cart)
    else: 
        cart = {}
    # Add or update the item in the cart
    if str(item_id) in cart:
        cart[str(item_id)]['quantity'] += 1  # Increment the quantity if item exists
    else:
        cart[str(item_id)] = {
            'item_name': item.item_name,
            'item_price': str(item.item_price),  # convert Decimal to string for JSON serialization
            'item_image_url': item.item_image.url if item.item_image else '',
            'quantity': 1
        }

    # Set the cookie with the updated cart
    response = JsonResponse({'success': True, 'message': 'Item added to cart'})
    response.set_cookie('cart', json.dumps(cart), max_age=3600*24*7)  # Cookie expires in 7 days
    return response


def notification(request): 
    context = {
        "url_name":"notification"
    }
    return render(request, "notification.html", context)