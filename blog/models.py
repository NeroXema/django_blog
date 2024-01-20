from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class CategoryModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PostModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(default=None, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

class CommentModel(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.content

class UserDetailModel(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.TextField()
    phone = models.IntegerField()
    birthday = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.user

class CategoryDetailModel(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    category = models.ManyToManyField(CategoryModel)

    def __str__(self):
        return self.description 