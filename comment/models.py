from django.db import models
from django.conf import settings


class Comment(models.Model):
    author = models.CharField(max_length=50)
    text = models.TextField()
    highlighted = models.TextField(default='')
    page_url = models.CharField(max_length=500, default='https://university.innopolis.ru/en/')

    def publish(self):
        self.save()


class URL(models.Model):
    site_url = models.CharField(max_length=500)


class Reply(models.Model):
    comment_id = models.IntegerField()
    author = models.CharField(max_length=50)
    text = models.TextField()

    def publish(self):
        self.save()
