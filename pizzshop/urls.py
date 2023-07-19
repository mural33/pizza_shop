from django.urls import path
from .import views
urlpatterns = [
    path("",views.home,name="home"),
    path("cart_save",views.cart_save,name="cart_item"),
    path("cart",views.cart,name="cart"),
    path("del_item",views.del_item,name="del"),
    path("order",views.order,name="order")
]
