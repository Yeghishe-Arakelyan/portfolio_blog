from django.db import models
from accounts.models import User
from django.urls import reverse
from django.utils.text import slugify


class PostCategory(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs): 
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=100, blank=False)
    name = models.CharField(max_length=100, blank=False)
    context = models.TextField(blank=True)
    content = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default=None)
    category = models.ManyToManyField(PostCategory, related_name='posts')
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self,):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)