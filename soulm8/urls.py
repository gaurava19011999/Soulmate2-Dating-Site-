from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import url
from django.urls import include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponseRedirect


urlpatterns = [
  #   url(r'^$', lambda r: HttpResponseRedirect('home')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('home.urls')),
    path('chatroom/', include('chatroom.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

