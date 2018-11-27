from django.urls import path
from . import views
urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'product/<int:id>/', views.product, name='product'),
    path('page-number-2/', views.second_page, name='second-page')
]


