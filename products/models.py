from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    meta_keywords = models.CharField("Meta Keywords",max_length=255, help_text='Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField("Meta Description", max_length=255, help_text='Content for description meta tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'categories'
        ordering = ['-created_at']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    image = models.ImageField(upload_to='photosProducts/')
    name = models.CharField(max_length=255, unique=True)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.CharField(max_length=30)
    code = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    stock = models.IntegerField()
    is_active = models.BooleanField()
    meta_keywords = models.CharField(max_length=255, help_text='Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField(max_length=255, help_text = 'Content for description meta tag')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)

    class Meta:
        db_table = 'products'
        ordering = ['-created_at']


    def __str__(self):
        return f"{self.name}"


class Tag(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"

class Product_card(models.Model):
    image = models.ImageField(upload_to='Products_card/')
    name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


class settings(models.Model):
    logo = models.ImageField(upload_to='settings/')
    def __str__(self):
        return "settings"

class Contacto(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.CharField(max_length=1000)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"
