from django.db import models
from django.urls import reverse_lazy
class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    condition = models.CharField(max_length=20, choices=[
        ('new', 'New'),
        ('used_good', 'Used but in good condition'),
        ('needs_repair', 'Needs repair')
    ])
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)
    uploader = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='uploaded_items')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('item_list')