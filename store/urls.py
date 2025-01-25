from django.urls import path
from store.views import product_catalog,category_list,view_cart,add_to_cart,remove_from_cart,view_orders,place_order


urlpatterns=[
    path('products/',product_catalog),
    path('categories/', category_list),
    path('cart/', view_cart),
    path('cart/add/',add_to_cart),
    path('cart/remove/',remove_from_cart),
    path('orders/',view_orders),
    path('orders/place/',place_order),
]
    


