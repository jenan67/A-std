from django.db import models
# Create your models here.
class project (models.Model):
  ProdFristName = models.TextField(max_length=50)
  prodLestName = models.DateField(max_length=50)
  ProdStdId = models.TimeField(max_length=50)
  ProdDateBit = models.DateField(max_length=50)
  ProdCurrentAge = models.DateField(max_length=50)
  ProdGdnder = models.DateField(max_length=50)
  ProdState =  models.TextField(max_length=50)
  Prodpostalcode = models.TextField(max_length=50)
  ProdEmail = models.EmailField(max_length=50)
  ProdTelephonenumber = models.TextField(max_length=50)
  prodmothertongue = models.TextField(max_length=50)
  Prodpaymentmethod = models.TextField(max_length=50)





    
