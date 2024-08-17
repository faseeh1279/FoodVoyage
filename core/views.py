from django.shortcuts import render 
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
    context = {"url_name":"OrderNow"}
    return render(request, "ordernow.html", context)

