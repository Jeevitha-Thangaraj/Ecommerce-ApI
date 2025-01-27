from django.urls import path
from store.views import product_catalog,get_category,create_category,category_list,view_cart,add_to_cart,remove_from_cart,view_orders,place_order


urlpatterns=[
    path('products/',product_catalog),
    path('get-categories/<int:id>/',get_category),
    path('create-categories/',create_category),
    path('list-categories/', category_list),
    path('cart/', view_cart),
    path('cart/add/',add_to_cart),
    path('cart/remove/',remove_from_cart),
    path('orders/',view_orders),
    path('orders/place/',place_order),
]
    


