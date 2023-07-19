from django.shortcuts import render
from django.http import HttpResponse
from .models import Shop,Type,Cart
from django.core import serializers
from django.http import JsonResponse
import json

def cart(req):
    try:
        data = Cart.objects.all()
        serialized_data = serializers.serialize('json', data)
        return JsonResponse(json.loads(serialized_data), safe=False)
    except Cart.DoesNotExist:
        return JsonResponse([], safe=False)
    
def home(req):
    items=Shop.objects.all()
    type=Type.objects.all()
    data=Cart.objects.all()
    l=Cart.objects.values_list("item")
    o=[i[0] for i in l]
    total=sum([i.count * i.price for i in Cart.objects.all()])
    return render(req,"shop/home.html",{"items":items,"type":type,"cart":data,"l":o,"total":total})

def cart_save(req):
    out=[]
    for i in Cart.objects.all():
        out+=[i.item]
    id=req.POST.get("item_id","")
    item_data=Shop.objects.get(id=id)
    if item_data.item not in  out:
        cart_item=Cart.objects.create(item=item_data.item,img=item_data.img,price=item_data.price)
        cart_item.save()
    else:
        cart_item=Cart.objects.get(item=item_data.item)
        cart_item.count+=1
        cart_item.save()
        # Call the cart function to activate it
    return HttpResponse("hi")

def del_item(req):
    print("del is activate")
    if req.method == "POST":
            del_id = req.POST.get("del_id", "")
            if del_id:
                name=Shop.objects.get(id=del_id)
                try:
                    cart = Cart.objects.get(item=name.item)
                    if cart.count > 1:
                        cart.count -= 1
                        cart.save()
                    else:
                        cart.delete()
                        # Call the cart function to activate it
                    return HttpResponse("Item deleted successfully")
                except Cart.DoesNotExist:
                        # Call the cart function to activate it
                    return HttpResponse("Cart item not found")
    return HttpResponse("Invalid request")

def order(req):
    return render(req,"shop/order.html")


