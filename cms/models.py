from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Client(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth_date = models.DateField()
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    joined_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-last_name", "first_name"]
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Carer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, default='Carer')
    clients = models.ManyToManyField(Client, related_name='carers')

    class Meta:
        ordering = ["-user__username"]

    def __str__(self):
        return self.user.username


class Note(models.Model):
    title = models.CharField(max_length=140, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="client_notes"
    )
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='notes', null=True, blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on",]

    def __str__(self):
        return f"{self.title} | for {self.client}"

"""
Pos. Note model for slugs if current slugs don't produce unique enough instances.
"""
# from django.db import models
# from django.utils.text import slugify
# from django.contrib.auth.models import User
# from datetime import datetime

# class Note(models.Model):
#     title = models.CharField(max_length=140, unique=True)
#     slug = models.SlugField(max_length=200, unique=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="client_notes")
#     client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='notes', null=True, blank=True)
#     content = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             # Combine the title with the date to form the slug
#             slug_str = f"{self.title} {self.created_on.strftime('%Y-%m-%d')}"
#             self.slug = slugify(slug_str)
#             # Handle potential slug duplicates
#             original_slug = self.slug
#             queryset = Note.objects.filter(slug=self.slug).exists()
#             count = 1
#             while queryset:
#                 self.slug = f"{original_slug}-{count}"
#                 count += 1
#                 queryset = Note.objects.filter(slug=self.slug).exists()
#         super(Note, self).save(*args, **kwargs)

#     def __str__(self):
#         return f"{self.title} | for {self.client}"