from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    first_paragraph = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='post', null=True, blank=True)
    register_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.title
