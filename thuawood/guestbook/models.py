import datetime
from django.db import models


class Entry(models.Model):
    name = models.CharField(
        max_length=200, blank=True,
        verbose_name="Namn")
    email = models.CharField(
        max_length=200, blank=True,
        verbose_name="E-post")
    homepage = models.URLField(
        blank=True,
        verbose_name="Hemsida")
    city = models.CharField(
        max_length=200, blank=True,
        verbose_name="Stad")
    comment = models.TextField(verbose_name="Kommentar")
    create_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True)

    def __str__(self):
        name = self.name or self.email or self.homepage or self.comment
        return name + self.create_date.strftime(' %Y/%m/%d')
