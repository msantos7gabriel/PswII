from django.urls import path
from . import views


urlpatterns = [
    path('', view=views.index, name='index-pessoa'),
    path('add/', view=views.add, name='add-pessoa'),
    path('remove/', view=views.remove, name='remove-pessoa'),
    path('update/', view=views.update, name='update-pessoa'),

]
