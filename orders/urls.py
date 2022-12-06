from django.urls import path
from . import views
urlpatterns = [
    path('place_order/',views.place_order,name='place_order'),
    path('payments/',views.payments,name = 'payments'),
    #path('handlerequest/',views.place_order.handlerequest,name='handlerequest'),
    path('order_complete/',views.order_complete,name='order_complete'),
]