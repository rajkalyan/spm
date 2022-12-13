from django.urls import path
from django.urls.resolvers import URLPattern
from Restaurant_app import views
from django.contrib.auth import views as v
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home,name="hm"),
    path('abt/',views.about,name="ab"),
    path('cnct/',views.contact,name="ct"),
    path('rg/',views.usrreg,name="reg"),
    path('additems/',views.additems,name="additems"),
    path('addstarter',views.addstarter,name="addstarter"),
    path('addbreads',views.addbreads,name="addbreads"),
    path('addrab',views.addrab,name="addrab"),
    path('accept',views.accept,name="accept"),
    path('oh',views.oh,name="oh"),
    path('bill',views.bill,name="bill"),
    path('login/',v.LoginView.as_view(template_name="app/login.html"),name="lg"),
    path('logout',v.LogoutView.as_view(template_name="app/logout.html"),name="lgo"),
    path('po',views.po,name="po"),
    path('od/<int:n>',views.od,name="od"),
    path('id/<int:n>',views.id,name="id"),
    path('iup/<int:n>',views.iup,name="iup"),
    path('orders',views.orders,name="orders"),
    path('roletype/',views.rolereq,name="rlrq"),
    path('gvper/',views.gveperm,name="gvpm"),
    path('gvup/<int:t>/',views.gvupd,name="gvup"),
    path('gvdel/<int:m>/',views.gvdel,name="gvdel"),
    path('pfle/',views.pfle,name="pf"),
    path('pfupd/',views.pfupd,name="pfupd"),
    path('fbd',views.feedback,name="fd"),
    path('chge/',views.changepwd,name="chpd"),
]