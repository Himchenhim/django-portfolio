from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=20)
    date = models.DateField()
    description = models.CharField(max_length=500)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title