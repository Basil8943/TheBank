from . import views
from django.urls import path
app_name='Bankapp'
urlpatterns=[
    path('',views.home,name="home"),
    path('branch/<int:b_id>/', views.detail, name="detail"),
    path('kalpeta',views.kalpeta,name="kalpeta"),
    path('mananthvady',views.mananthvady,name="mananthvady"),
    path('bathery',views.bathery,name="bathery"),
    path('koduvally',views.koduvally,name="koduvally"),
    path('tmsry',views.tmsry,name="tmsry"),
    path('medc',views.medc,name="medc"),
    path('kaloor',views.kaloor,name="kaloor"),
    path('aluva',views.aluva,name="aluva"),
    path('kakkanad',views.kakkanad,name="kakkanad"),
]