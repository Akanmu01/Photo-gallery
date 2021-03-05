from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


CATEGORY_CHOICES = (
    ('BACKGROUND', 'background'),
    ('LOGO', 'logo')
)

class Upload(models.Model):
    author = models.ForeignKey(User, default=1, related_name="user_post", on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=40)
    image = models.ImageField(upload_to='images/')
    # category = models.CharField(choices=CATEGORY_CHOICES, default='BACKGROUND', max_length=10)
    slug = models.SlugField(unique=True, max_length=100)
    tags = TaggableManager()

    def __str__(self):
    	return self.title
 