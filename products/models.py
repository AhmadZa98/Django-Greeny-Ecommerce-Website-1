from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

FLAG_TYPE = (
    ("New","New"),
    ("Feature","Feature"),
)

class Product(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    sku = models.IntegerField(_("SKU"))
    brand = models.ForeignKey("Brand",verbose_name=("Brand"),related_name="product_brand", on_delete=models.SET_NULL, null = True, blank=True)
    price = models.FloatField(_("Price"))
    desc = models.TextField(max_length=10000)
    tags = ""
    flag = models.CharField(max_length=10,choices=FLAG_TYPE)
    category = models.ForeignKey("Category",verbose_name=("Category"),related_name="product_category", on_delete=models.SET_NULL, null = True, blank=True)
    def __str__(self):
        return self.name


class ProductImages(models.Model):
    product = models.ForeignKey(Product, verbose_name = _("Product"),related_name="product_image", on_delete=models.CASCADE)    
    image = models.ImageField(_("image"),upload_to = "product/")
    def __str__(self):
        return str(self.product)

class Brand(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(_("Name"),max_length=50)
    image = models.ImageField(upload_to="Category/")
    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(User, verbose_name = _("User"),related_name="review_author", on_delete=models.SET_NULL, null = True, blank=True)
    product = models.ForeignKey(Product, verbose_name=_("Product"), related_name="product_review",on_delete=models.SET_NULL , null = True, blank=True)
    review = models.TextField(_("Review"), max_length=500)
    rate = models.IntegerField(_("Rate"),validators=[MaxValueValidator(5),MinValueValidator(0)])
    created_at = models.DateTimeField(_("Create at"),default=timezone.now)
    def __str__(self):
        return f"{self.user.username} - {self.product.name}"