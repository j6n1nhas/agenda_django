from django.urls import path
from . import views


urlpatterns = [path('', views.index, name='index'),
               path('<int:id>', views.detalhe, name='detalhe'),
               path('busca/', views.busca, name='busca'),
               ]