from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('blog.html', views.blog, name='blog'),
	path('',include('pages.urls')),
	path('listings/',include('listings.urls')),
    path('accounts/',include('accounts.urls')),
     path('agent/',include('agent.urls')),
    path('booking/',include('booking.urls')),
    path('property/',include('property.urls')),
    path('contacts/',include('contacts.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
