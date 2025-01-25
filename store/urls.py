from django.urls import path
from store.views import create_category,get_categories,create_product,get_products,list_products,place_order


urlpatterns=[
    path('create-category/',create_category),
    path('get-category<int:id>/',get_categories),
    path('create-product<int:id>/',create_product),
    path('get-product/',get_products),
    path('list-product/',list_products),
    path('place-oder/',place_order),
    


]