from django.shortcuts import render, HttpResponse
from restaurant.models import AddFood
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from . import models 
def index(request):
    items = AddFood.objects.all() 
    context = {"url_name":"Home", "queryset":items}
    return render(request, 'customer/index.html', context)

@csrf_exempt
def add_to_cart(request): 
    if request.method == 'POST':
        itemId = request.POST.get('itemId')
        queryset = AddFood.objects.get(id = itemId)
        models.AddToCart.objects.create(item_name = queryset.item_name, item_price = queryset.item_price, item_image = queryset.item_image)
        return JsonResponse({"Message":"Successfully Added Data"})
    else: 
        return JsonResponse({"Message":"Invalid Request"})

def notification(request): 
    context = {
        "url_name":"notification"
    }
    return render(request, "notification.html", context)

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

# setting a cookie 
# def view(reqeust): 
#     response = HttpResponse('blah')
#     response.set_cookie('cookie_name', 'cookie_value')


# # reteriving a cookie 
# def view(reqeust): 
#     value = reqeust.COOKIES.get('cookie_name') 
#     if value is None: 
#         # Cookie is not set 
#         print("") 
        
#     # OR 
#     try:
#         value = request.COOKIES['cookie_name']
#     except KeyError:
#     # Cookie is not set
#         print("")
        