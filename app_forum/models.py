from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField()

    # has many threads


class Thread(models.Model):
    text = models.TextField()
    title = models.CharField(max_length=100)
    created = models.DateTimeField()

    # has one category
    # has many comments

class Comment(models.Model):
    likes = models.IntegerField()
    text = models.TextField()
    # has many recipients (users)
    has_been_read = models.BooleanField(default=False)
    direct_comment = models.BooleanField(default=False)
    created = models.DateTimeField()
