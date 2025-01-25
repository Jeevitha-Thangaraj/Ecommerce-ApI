from django.urls import path
from authentication.views import signup_user,login_user,get_user

urlpatterns=[
    path('sign-up/',signup_user),
    path('login/',login_user),
    # path('logout/',logout_view)
    path('get/<int:id>/',get_user)

]