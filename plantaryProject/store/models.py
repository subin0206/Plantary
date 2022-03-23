from django.db import models

# Store
class Product(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    price = models.DecimalField(max_digits=10, decimal_places=0)
    body = models.TextField()
    images = models.ImageField(blank=True, upload_to="images/", null=True)

    def __str__(self):
        return self.title

class Photo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)