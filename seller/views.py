from django.shortcuts import render, redirect
from .models import Food
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

@login_required
def seller_index(request):
    foods = Food.objects.filter(user = request.user)
    context = {
        'object_list' : foods
    }
    return render(request, template_name='seller/seller_index.html', context = context)

@login_required
def add_food(request):
    # get
    if request.method=='GET':
        return render(request, 'seller/seller_add_food.html')
    # post
    elif request.method=="POST":
        # 폼에서 전달되는 각 값을 뽑아와서 DB에 저장

        # Food 내용을 구성 영역
        # category = Category.objects.get(name=request.POST['category'])
        user=request.user
        food_name = request.POST['name']
        food_price = request.POST['price']
        food_description = request.POST['description']

        # 이미지 저장 및 url 설정 내용
        fs=FileSystemStorage()
        uploaded_file = request.FILES['file']
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)

        Food.objects.create(user= user,name=food_name, price =food_price , description=food_description,image_url=url)    

    return redirect('seller:seller_index')

@login_required
def food_detail(request, pk):
    object = Food.objects.get(pk=pk)
    context = {
        'object' : object
    }
    return render(request, 'seller/seller_food_detail.html', context=context)

@login_required
def food_delete(request, pk):
    object = Food.objects.get(pk=pk)
    object.delete()
    return redirect('seller:seller_index')