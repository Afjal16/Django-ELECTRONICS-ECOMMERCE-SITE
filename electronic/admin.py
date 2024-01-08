from django.contrib import admin
from .models import Categorie,Brand,Color,Filter_price,Product,Images,Tag,Contact,orderItem,Order

# Register your models here.

class ImagesTublerinline(admin.TabularInline):
    model=Images
    
class TagTublerinline(admin.TabularInline):
    model=Tag
    
class ProductAdmin(admin.ModelAdmin):
    inlines=[ImagesTublerinline,TagTublerinline]


class orderItemTublerinline(admin.TabularInline):
    model=orderItem
    
class OrderAdmin(admin.ModelAdmin):
    inlines = [orderItemTublerinline]




admin.site.register(Categorie)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Filter_price)
admin.site.register(Product,ProductAdmin)

admin.site.register(Images)
admin.site.register(Tag)


admin.site.register(Contact)

admin.site.register(orderItem)
admin.site.register(Order,OrderAdmin)

