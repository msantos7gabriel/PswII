from django.contrib import admin
from django.urls import path, include
from pessoas.views import index_redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pessoa/', include('pessoas.urls')),
    path('', view=index_redirect,),
]
