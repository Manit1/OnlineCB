from django.urls import path
from auth1 import views

urlpatterns=[
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout_view)
]