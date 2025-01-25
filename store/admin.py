from django.contrib import admin
from store.models import Category,Product,Customer,Cart,Order

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)


# Register your models here.
