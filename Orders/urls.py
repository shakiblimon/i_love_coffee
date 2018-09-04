from django.urls import path, include
from django.conf.urls import url

from . import views

urlpatterns = [
    path('',views.OrderList.as_view()),
    path('<int:pk>/',views.OrderDetails.as_view()),
    path('view/',views.ViewHistory.as_view()),
    path('usr/',include('rest_auth.urls')),

    path('usr/rg/',include('rest_auth.registration.urls')),


]