from django.shortcuts import render,redirect
from electronic.models import Product,Categorie,Filter_price,Color,Brand,Contact,Order,orderItem
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
#cart===
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
#cart===


# Create your views here.
def Home(request):
    products=Product.objects.filter(status='PUBLISH')
    
    context={
        'products':products,
    }
    return render(request, 'main/home.html',context)

def About(request):
    return render(request, 'main/about.html')

def Blog(request):
    return render(request, 'main/blog.html')

def Products(request):
    # product=Product.objects.filter(status='PUBLISH')
    categorie=Categorie.objects.all()
    filter_price=Filter_price.objects.all()
    colors=Color.objects.all()
    brands=Brand.objects.all()
    
    CATID=request.GET.get('categorie')# HTML link  name'categories'
    FILTER_PRICE_ID=request.GET.get('filter_price')# HTMLlink  name'filter_price'
    COLOR_ID=request.GET.get('colors')# HTML link  name'filter_price'
    BRAND_ID=request.GET.get('brands')# HTML link  name'filter_price'
    
    ATOZID=request.GET.get('ATOZ')
    ZTOAID=request.GET.get('ZTOA')
    
    
    if CATID:
        product=Product.objects.filter(categories=CATID,status='PUBLISH')# models forenkey name 'categories'
    elif FILTER_PRICE_ID:
        product=Product.objects.filter(filter_price=FILTER_PRICE_ID,status='PUBLISH')# models forenkey name 'filter_price'
    elif COLOR_ID:
        product=Product.objects.filter(color=COLOR_ID,status='PUBLISH')# models forenkey name 'colors'
    elif BRAND_ID:
        product=Product.objects.filter(brand=BRAND_ID,status='PUBLISH')# models forenkey name  'brand' 
        
           
    elif ATOZID:
        product=Product.objects.filter(status='PUBLISH').order_by=('name')# models  name
    elif ZTOAID:
        product=Product.objects.filter(status='PUBLISH').order_by=('-name')# models  name
         
    else:
        product=Product.objects.filter(status='PUBLISH')
        
    
    context={
        'product':product,
        'categorie':categorie,
        'filter_price':filter_price,
        'colors':colors,
        'brands':brands,
    }
    return render(request, 'main/product.html',context)

def Search(request):
    search=request.GET.get('search')
    product=Product.objects.filter(name__icontains=search)
    price=Product.objects.filter(price__icontains=search)
    context={
        'product':product,
        'price':price,
    }
    return render(request, 'main/search.html', context)

def Product_details_page(request,id):
    product=Product.objects.filter(id=id).first()
    context={
        'product':product,        
    }
    return render(request, 'main/product_single.html',context)

def Contacts(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contacts_view=Contact(name=name,email=email,subject=subject,message=message)

        subject=subject
        message=message
        email_from=settings.EMAIL_HOST_USER       
        try :
            send_mail(subject,message,email_from,['afjalhossen199@gmail.com'])
            contacts_view.save()
            return redirect('home')
        except:
            return redirect('contact')
         
    return render(request, 'main/contact.html')

#Authentication start============================================================
def handleRegister(request):
    if request.method=='POST':
        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass12')
        
        register_views=User.objects.create_user(username,email,pass1)
        register_views.first_name=first_name
        register_views.last_name=last_name
        register_views.save()
        return redirect('register')
    
    return render(request, 'registration/auth.html')

def handleLogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('login')
         
    return render(request, 'registration/auth.html')

def handleLogout(request):
    logout(request)
    return redirect('home')
#Authentication end============================================================

# def Cart(request):
#     return render(request, 'cart/cart_details.html')
#=======cart===============

@login_required(login_url="/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url="/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_detail(request):
    return render(request, 'cart/cart_details.html')


def Checkout(request):
    return render(request, 'cart/checkout.html')


def Placeorder(request):
    if request.method=="POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        country=request.POST.get('country')
        address=request.POST.get('address')
        city=request.POST.get('city')
        state=request.POST.get('state')
        Postcode=request.POST.get('Postcode')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        additional_info=request.POST.get('additional_info')
        custumer_info_views=Order()
        
        
    return render(request, 'cart/placeorder.html')
#=======cart===============


