from django.urls import path 
from . import views

urlpatterns = [
    path('api/', views.api, name='api'),
    path('school/', views.school, name='school'),
    path('login/', views.login, name='login'),
    path('message/', views.message, name='message'),
    path('register/', views.register, name='register'),
    path('portal/', views.portal, name='portal'),
    path('messages_view/', views.messages_view, name='messages_view'),
    path('admin1/', views.admin1, name='admin1'),
    path('messages_send/', views.messages_send, name='messages_send'),
    path('deregister/', views.deregister, name='deregister'),
    path('form1/', views.form1, name='form1'),
    path('store/<str:name>/', views.store, name='store'),
    path('bus/', views.bus, name='bus'),
    path('music/', views.music, name='music'),
    path('rest_store/', views.rest_store, name='rest_store'),
    path('forest/', views.forest, name='forest'),
    path('boot/', views.boot, name='boot'),
    path('addMarks/', views.addMarks, name='addMarks'),
    path('coins/', views.coins, name='coins'),
    path('speed/<int:age>/', views.speed, name='speed'),
    path('coinLogin1/', views.coinLogin1, name='coinLogin1'),
    path('near_shop/<str:shop>/', views.near_shop, name='near_shop'),
   
]