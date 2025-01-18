from datetime import datetime

from django.db.models import Q, F
from django.shortcuts import render
import logging

from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import City, Street, Shop
from .serializers import CitySerializer, StreetSerializer, ShopSerializer


class CityView(APIView):
    def get(self, request):
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)


class StreetView(APIView):
    def get(self, request, city_id):
        streets = Street.objects.filter(city_id=city_id)
        serializer = StreetSerializer(streets, many=True)
        return Response(serializer.data)


class ShopView(APIView):
    def get(self, request):
        street = request.query_params.get('street', None)
        city = request.query_params.get('city', None)
        open_status = request.query_params.get('open', None)

        shops = Shop.objects.all()

        if street:
            shops = shops.filter(street__title__exact=street)
        if city:
            shops = shops.filter(city__title__exact=city)
        if open_status is not None:
            current_time = timezone.localtime(timezone.now()).time()
            condition = (Q(opening_time__lte=current_time, closing_time__gte=current_time) |
                         Q(opening_time__gt=F("closing_time"), opening_time__lte=current_time) |
                         Q(opening_time__gt=F("closing_time"), closing_time__gte=current_time))

            if open_status == '1':
                shops = shops.filter(condition)

            else:
                shops = shops.exclude(condition)

        serializer = ShopSerializer(shops, many=True)
        return Response(serializer.data)

    def post(self, request):
        title = request.data.get('title')
        opening_time = request.data.get('opening_time')
        closing_time = request.data.get('closing_time')
        city_id = request.data.get('city_id')
        street_id = request.data.get('street_id')

        try:
            city = City.objects.get(id=city_id)
            street = Street.objects.get(id=street_id)
        except City.DoesNotExist:
            return Response({"error": "City not found"}, status=status.HTTP_400_BAD_REQUEST)
        except Street.DoesNotExist:
            return Response({"error": "Street not found"}, status=status.HTTP_400_BAD_REQUEST)

        if street.city.id != city.id:
            return Response({"error": "Street does not belong to the specified city"},
                            status=status.HTTP_400_BAD_REQUEST)

        shop = Shop.objects.create(
            title=title,
            opening_time=opening_time,
            closing_time=closing_time,
            city=city,
            street=street
        )

        return Response({"id": shop.id}, status=status.HTTP_201_CREATED)
