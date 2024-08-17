from django.shortcuts import render

def index(request):
    context = {"url_name":"Home"}
    return render(request, 'customer/index.html', context)
