from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingSatus"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>/", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
]