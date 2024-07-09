from django.db import models

from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User

# Create your models here.

class BlogAuthor(models.Model):
    """Model representing an author."""
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["user","bio"]

    def get_absolute_url(self):
        """Returns the url to access a particular blog author """
        return reverse('blogs-by-author', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.user.username}'
    