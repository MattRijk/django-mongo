from django.db import models
from djangotoolbox.fields import EmbeddedModelField

from djangotoolbox.fields import ListField

class Snippit(models.Model):
    text = models.TextField()

class Post(models.Model):
    title = models.CharField()
    text = models.TextField()
    tags = ListField()
    comments = ListField()
    snippits = ListField(EmbeddedModelField('Snippit'))
