from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    # has many threads


class Thread(models.Model):
    text = models.TextField()
    title = models.CharField(max_length=100)
    modified = models.DateTimeField()
    is_message_thread = models.BooleanField(default=False)

    # has one owner
    created_by = models.ForeignKey(User)

    # has one category
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # has many comments

    class Meta:
        ordering = ('modified',)

class Comment(models.Model):
    likes = models.IntegerField(default=0)
    text = models.TextField()
    has_been_read = models.BooleanField(default=False)
    message_comment = models.BooleanField(default=False)
    created = models.DateTimeField()

    # has one owner (comments)
    created_by = models.ForeignKey(User, related_name="messages_sent")

    # has many recipients (users)
    recipients = models.ManyToManyField(User, related_name="messages_received")

    # has one Thread
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)
