from django.db import models
from datetime import date
# Create your models here.
from django.urls import reverse


class District(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Branch(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    img= models.ImageField(upload_to='pics')

    def get_url(self):
        return reverse('Bankapp:detail',args=[self.id])

    def __str__(self):
        return self.name


class Application(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'), ('Female', 'Female'),)
    Accounts = (
            ('SavingsAccount', 'SavingsAccount'), ('SalaryAccount', 'SalaryAccount'), ('CreditAccount', 'CreditAccount'),)
    name=models.CharField(max_length=100)
    age=models.CharField(max_length=10)
    birth_date=models.DateField()
    mobile=models.CharField(max_length=25)
    email=models.EmailField(max_length=150)
    address=models.TextField()
    gender=models.CharField(max_length=10,choices=GENDER_CHOICES,default=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, blank=True, null=True)
    m_name = models.CharField(max_length=100,default=True)
    acc_type=models.CharField(choices=Accounts,max_length=100,default=True)

    def __str__(self):
        return self.name