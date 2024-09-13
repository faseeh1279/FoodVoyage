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