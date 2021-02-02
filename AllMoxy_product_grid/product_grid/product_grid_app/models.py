from django.db import models

# Create your models here.
class product_manager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        if len(post_data['title']) < 2:
            errors['title'] = "Title must be at least 2 characters"
        if len(post_data['desc']) < 10:
            errors['desc'] = "Description must be at least 10 characters"
        if len(post_data['price']) < 0.01:
            errors['price'] = "Price must be at least 1 cent"
        if len(post_data['quantity']) < 1:
            errors['quantity'] = "quantity must be at least 1"
        return errors

class product(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = product_manager()