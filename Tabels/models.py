from django.db import models
import datetime

# Create your models here.
class Month_Field(models.Model):
    Month_Title         = models.CharField(max_length=200)

    def __str__(self):
        return self.Month_Title




class Taluk_Field(models.Model):
    Taluk_Title         = models.CharField(max_length=200)

    def __str__(self):
        return self.Taluk_Title



class HeadAccount_Field(models.Model):
    Account_Title       = models.CharField(max_length=500)

    def __str__(self):
        return self.Account_Title

YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))
    
class Tabel_Data(models.Model):
    Data_Title          = models.CharField(max_length=200)
    Taluk               = models.CharField(max_length=200)
    Year                = models.IntegerField(('year'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    Month               = models.CharField(max_length=200)
    Account             = models.CharField(max_length=200)

    def __str__(self):
        return self.Data_Title

