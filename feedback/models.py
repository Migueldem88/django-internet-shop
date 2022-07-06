from django.db import models
from shop.models import Product

class Feedback(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    direccion = models.CharField(max_length=250)
    codigo_postal = models.CharField(max_length=20)
    mensaje = models.CharField(max_length=5000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Feedback {self.id}'

class FeedbackItem(models.Model):
    comment = models.ForeignKey(Feedback,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='feedback_items',
                                on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)