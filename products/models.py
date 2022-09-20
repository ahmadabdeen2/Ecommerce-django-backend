from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from core.models import Profile
# Create your models here.
class Product(models.Model):
    CHOICES_CATEGORY = [
        ('Men', 'Men'),
        ('Women', 'Women'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100, choices=CHOICES_CATEGORY)
    
    image = models.ImageField(upload_to='images/')
    price = models.FloatField()
    stock_left = models.IntegerField()
    def no_of_ratings(self):
        ratings = Rating.objects.filter(product=self)
        return len(ratings)
    def avg_rating(self):
        sum = 0
        ratings = Rating.objects.filter(product=self)
        for rating in ratings:
            sum += rating.rating
        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0
    def __str__(self):
        return str(self.name)

class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])

    class Meta:
        unique_together = (('user', 'product'),)
        index_together = (('user', 'product'),)

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return " Order " + str(self.id)

class OrderItem(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderitems_set')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self._id)
