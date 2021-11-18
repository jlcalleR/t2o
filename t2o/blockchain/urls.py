from django.contrib import admin
from django.urls import path, include
from blockchain import views


urlpatterns = [
    path('save_orders/<str:crypto>-<str:fiat>/', views.save_orders),
    path('specific_statistics/<str:type_of_order>/<str:crypto>-<str:fiat>/', views.order_statistics),
    path('general_statistics/', views.general_statistics),
]

