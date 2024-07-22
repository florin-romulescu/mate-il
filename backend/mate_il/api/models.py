from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    attachments = models.ManyToManyField('Attachment', blank=True)
    external_url = models.URLField(blank=True, null=True)

    @property
    def has_attachment(self):
        return self.attachments is not None

class Attachment(models.Model):
    attachment = models.FileField(upload_to='files/')

class Announce(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)