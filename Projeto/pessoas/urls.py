from django.urls import path
from . import views


urlpatterns = [
    path('', view=views.index, name='index-pessoa'),
    path('add/', view=views.add, name='add-pessoa'),
    path('detalhe/<pk>/', view=views.detalhe, name='detalhe-pessoa'),
    path('remove/<int:pk>/', view=views.remove, name='remove-pessoa'),
    path('edit/<int:pk>/', view=views.update, name='edit-pessoa'),

]
