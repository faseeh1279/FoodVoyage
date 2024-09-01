"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from django.conf import settings 
from . import views 
from django.conf.urls.static import static 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")), 
    # Core URL's
    path('about/', views.about_page, name='about'),
    path('contact/', views.contact_us, name='contact'), 
    path('services/', views.services_page, name='services'),
    path('order-now/', views.order_now, name='order'), 
    path("view-cart/", views.view_cart, name="view-cart"),
     


    # AJAX 
    path('load-more-posts/', views.load_more_posts, name='load_more_posts'),
   

    # External Apps 
    path('home/', include('users.urls')), 
    path('', include('customer.urls')), 
    path("partner-with-us/restaurant/", include("restaurant.urls")), 
    path("partner-with-us/rider/", include("rider.urls")),
    path("view-cart/payment/", include("payment.urls")), 
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()