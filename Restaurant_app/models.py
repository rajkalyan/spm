
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    age = models.IntegerField(default=20)
    mobilenumber = models.CharField(max_length=10,null=True)
    uimg = models.ImageField(upload_to='Profilepics/', default = 'logo.png')
    t = [(1,'Guest'),(2,'Manager'),(3,'User')]
    role = models.IntegerField(choices=t,default=1)

class Rolereq(models.Model):
    f = [(2,'Manager'),(3,'User')]
    rltype = models.IntegerField(choices=f)
    is_checked = models.BooleanField(default=False)
    Uname = models.CharField(max_length=50)
    ud = models.OneToOneField(User,on_delete=models.CASCADE)

class Starters(models.Model):
    y=[('Select item-type', 'Select item-type'),('Hair cut','Hair cut'),('Hair spa', 'Hair spa'),('Skin care', 'Skin care')] 
    sname=models.CharField(max_length=50)
    scategory=models.CharField(choices=y,default="Select item-type",max_length=50)
    sprice=models.DecimalField(decimal_places=3,max_digits=10)
    simage=models.ImageField(upload_to='Itemimages/',default='logo.png')

    def __str__(self):
        return self.bname

class Breads(models.Model): 
    bname=models.CharField(max_length=50)
    bprice=models.DecimalField(decimal_places=3,max_digits=10)

    def __str__(self):
        return self.bname

class Rice(models.Model):
    y=[('Select item-type', 'Select item-type'),('Sofa','Sofa'),('Bed', 'Bed')] 
    rbname=models.CharField(max_length=50)
    rbcategory=models.CharField(choices=y,default="Select item-type",max_length=50)
    rbprice=models.DecimalField(decimal_places=3,max_digits=10)

    def __str__(self):
        return self.rbname

class Order(models.Model):
    name=models.CharField(max_length=50)
    quantity=models.IntegerField()
    price=models.DecimalField(decimal_places=3,max_digits=10)
    uid = models.ForeignKey(User,on_delete=models.CASCADE)

class Manageorders(models.Model):
    uname=models.CharField(max_length=50)
    tname=models.CharField(max_length=5000000)
    items=models.CharField(max_length=5000000)

class Orderhistory(models.Model):
    items=models.CharField(max_length=5000000)
    billamoubt=models.DecimalField(decimal_places=3,max_digits=10)
    cid = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    time = models.DateTimeField(null=True,auto_now=True)

