from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('checkout', views.checkout, name='checkout'),
    path('thank_you/<int:id>', views.thank_you, name='thank_you')
]
