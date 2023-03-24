from datetime import timezone
from django.db import models

# Create your models here.   
class Addres(models.Model):
    #id= models.BigAutoField(primary_key=True)
    number= models.IntegerField()
    stratName= models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    country= models.CharField(max_length=100)
    postCode= models.PositiveIntegerField()
    def __str__(self):
        return self.city

class Editor(models.Model):
    #id= models.BigAutoField(primary_key=True)
    name= models.CharField(max_length=100, unique=True)
    website = models.URLField()
    email = models.EmailField()
    TelephoneNumber = models.CharField(max_length=20)
    # describe the relashionship between Editor and Adress(one-to-one):
    Addres =models.OneToOneField(Addres, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name
    
class Book(models.Model):
    isbnCode = models.CharField(max_length=20, primary_key=True, default='0000')
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=1)
    nbPages = models.PositiveIntegerField(default=0)
    cover = models.ImageField(upload_to='potos/', null=True, blank=True)
    #the default releadeDate field is the current date
    releaseDate = models.DateField(auto_now_add=True, null=True, blank=True)
    #relaseDate = models.DateField(default=timezone.now)
    # describe the relashionship between Editor and Adress(many-to-one):
    Editor= models.ForeignKey(Editor, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.title
    
class Author(models.Model):
    #id= models.BigAutoField(primary_key=True)
    name=  models.CharField(max_length=100)
    nationality=  models.CharField(max_length=100)
    description=  models.TextField(null=True, blank=True)
    # describe the relashionship between Editor and Adress(many-to-many):
    #writing is the name of association table
    writing= models.ManyToManyField(Book)
    def __str__(self):
        return self.name





