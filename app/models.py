from django.db import models


class City(models.Model):
    title = models.CharField(max_length=100, unique=True)

    class Meta:
        app_label = 'app'

    def __str__(self):
        return self.title


class Street(models.Model):
    title = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        app_label = 'app'
        unique_together = ('title', 'city')

    def __str__(self):
        return self.title


class Shop(models.Model):
    title = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    class Meta:
        app_label = 'app'
        unique_together = ('title', 'city', 'street')

    def __str__(self):
        return f"{self.title} ({self.street.title}, {self.city.title})"
