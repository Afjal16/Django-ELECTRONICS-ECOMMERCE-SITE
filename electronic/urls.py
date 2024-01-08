from django.urls import path
from electronic import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('products/', views.Products, name='products'),
    path('product_details/<str:id>', views.Product_details_page, name='product_details'),
    
    path('search/', views.Search, name='search'),
    path('contact/', views.Contacts, name='contact'),
    path('about/', views.About, name='about'),
    path('blog/', views.Blog, name='blog'),
    
    path('register/', views.handleRegister, name='register'),
    path('login/', views.handleLogin, name='login'),
    path('logout/', views.handleLogout, name='logout'),
    
    #path('cart/cart_detail/', views.Cart, name='cart_details'),
    #============Cart============================
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    
    path('cart/checkout/',views.Checkout,name='checkout'),
    path('cart/checkout/placeorder',views.Placeorder,name='placeorder'),
    #============Cart============================
    
    
]