from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=12)


class Review(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    text = models.CharField(max_length=140)
    image = models.FilePathField(max_length=20)
