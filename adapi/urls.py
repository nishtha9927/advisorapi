from django.contrib import admin
from django.urls import path,include
from .views import advisor_add_view,userview,userloginview,advisorlistview,bookcall,booked

urlpatterns = [
    path('admin/advisor/',advisor_add_view ),
    path('user/register/',userview),
    path('user/login/',userloginview),
    path('user/<int:userid>/advisor',advisorlistview),
    path('user/<str:userid>/advisor/<int:advisorid>/',bookcall ),
    path('user/<int:userid>/advisor/booking/',booked),


    
]
