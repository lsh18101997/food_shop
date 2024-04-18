from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib.auth.models import User
from seller.models import Food
from .models import Cart

def order_detail(request, pk):
    object = Food.objects.get(pk=pk)
    context = {
        'object' : object
    }
    return render(request, 'order/order_food_detail.html', context=context)

from django.http import JsonResponse
@login_required
def modify_cart(request):
    user_id= request.POST['userId']
    user = User.objects.get(pk=user_id)
    food_id= request.POST['foodId']
    food = Food.objects.get(pk=food_id)
    cart, _ = Cart.objects.get_or_create(user=user, food=food)    
    cart.amount+=int(request.POST['amountChange'])
    if cart.amount>0:
        cart.save()
    # 변경된 최종 결과를 반환(JSON)
    totalQuantity = user.cart_set.aggregate(totalcount=Sum('amount'))['totalcount']
    context = {
        'newQuantity':cart.amount, 
        'totalQuantity' : totalQuantity,
        'message':'수량이 성공적으로 업데이트 되었습니다.',
        'success':True
    }
    return JsonResponse(context)

@login_required
def order_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    food = [Food.objects.get(pk=i.food_id) for i in cart]
    context = {
        'object_list' : food
    }
    return render(request, 'order/order_cart.html', context=context)
