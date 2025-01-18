from django.urls import path
from .views import CityView, StreetView, ShopView


urlpatterns = [
    path('city/', CityView.as_view(), name='city-list'),
    path('city/<int:city_id>/street/', StreetView.as_view(), name='street-list'),
    path('shop/', ShopView.as_view(), name='shop'),

]
