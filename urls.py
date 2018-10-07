from django.urls import path

from . import views
from . import payment


urlpatterns = [
    path('', views.index, name='index'),
    path('order/', views.ordering, name='order'),
    path('pay/', payment.creditCardPayment, name='card'),

]
