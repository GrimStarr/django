from django.urls import path
from .import views

urlpatterns = [
    path('gold/<slug:type>/<slug:stoploss>/', views.buy),
    path('gold/<slug:type>/<slug:stoploss>/<slug:repeat>/', views.buy)
]