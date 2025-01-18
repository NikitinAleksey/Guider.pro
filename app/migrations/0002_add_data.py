# Generated by Django 5.1.5 on 2025-01-17 12:00

import django.db.models.deletion
from django.db import migrations, models


def create_initial_data(apps, schema_editor):
    City = apps.get_model('app', 'City')
    Street = apps.get_model('app', 'Street')
    Shop = apps.get_model('app', 'Shop')

    cities = [
        "San José", "Alajuela", "Cartago", "Heredia", "Puntarenas",
        "Limón", "Guanacaste", "Pérez Zeledón", "San Carlos", "Liberia"
    ]

    streets_data = {
        "San José": [
            "Avenida Central", "Calle 1", "Calle 2", "Avenida 10", "Calle 5",
            "Calle 7", "Calle 9", "Avenida 3", "Calle 15", "Avenida 8"
        ],
        "Alajuela": [
            "Avenida 2", "Calle 3", "Calle 4", "Avenida 15", "Calle 6",
            "Calle 8", "Avenida 12", "Calle 14", "Avenida 7", "Calle 10"
        ],
        "Cartago": [
            "Avenida 1", "Calle 5", "Calle 9", "Avenida 6", "Calle 11",
            "Calle 3", "Avenida 4", "Calle 12", "Avenida 9", "Calle 7"
        ],
        "Heredia": [
            "Calle 2", "Avenida 4", "Calle 6", "Calle 8", "Avenida 5",
            "Calle 10", "Avenida 3", "Calle 12", "Calle 14", "Avenida 7"
        ],
        "Puntarenas": [
            "Calle 1", "Avenida 5", "Calle 3", "Avenida 8", "Calle 4",
            "Calle 9", "Avenida 2", "Calle 10", "Avenida 6", "Calle 7"
        ],
        "Limón": [
            "Calle 5", "Avenida 9", "Calle 2", "Avenida 7", "Calle 4",
            "Avenida 10", "Calle 6", "Avenida 3", "Calle 1", "Calle 8"
        ],
        "Guanacaste": [
            "Calle 3", "Avenida 4", "Calle 1", "Avenida 5", "Calle 7",
            "Calle 9", "Avenida 2", "Calle 6", "Avenida 12", "Calle 10"
        ],
        "Pérez Zeledón": [
            "Avenida 6", "Calle 8", "Calle 7", "Avenida 4", "Calle 3",
            "Avenida 2", "Calle 1", "Calle 9", "Avenida 10", "Calle 5"
        ],
        "San Carlos": [
            "Avenida 3", "Calle 2", "Avenida 8", "Calle 4", "Calle 10",
            "Avenida 1", "Calle 7", "Avenida 5", "Calle 6", "Calle 12"
        ],
        "Liberia": [
            "Avenida 5", "Calle 6", "Calle 2", "Avenida 3", "Calle 10",
            "Avenida 8", "Calle 7", "Avenida 4", "Calle 1", "Calle 9"
        ]
    }

    city_objects = {}
    for city_name in cities:
        city = City.objects.create(title=city_name)
        city_objects[city_name] = city

    for city_name, city in city_objects.items():
        for street_name in streets_data[city_name]:
            Street.objects.create(title=street_name, city=city)

    for city_name, city in city_objects.items():
        streets_in_city = Street.objects.filter(city=city)
        for street in streets_in_city[:3]:  # Создадим по 3 магазина для каждого города
            Shop.objects.create(title=f"Shop 1 {city_name}", opening_time="08:00:00", closing_time="18:00:00",
                                city=city, street=street)
            Shop.objects.create(title=f"Shop 2 {city_name}", opening_time="09:00:00", closing_time="17:00:00",
                                city=city, street=street)


class Migration(migrations.Migration):
    initial = False

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_data),
    ]
