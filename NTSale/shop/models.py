from django.db import models

class Categories(models.Model):
    CategoryID = models.AutoField(primary_key=True)
    CategoryName = models.CharField(max_length=255)
    Description = models.TextField(null=True, blank=True)
    Picture = models.BinaryField(null=True, blank=True)

    def __str__(self):
        return self.CategoryName

class Suppliers(models.Model):
    SupplierID = models.AutoField(primary_key=True)
    CompanyName = models.CharField(max_length=255)
    ContactName = models.CharField(max_length=255, null=True, blank=True)
    ContactTitle = models.CharField(max_length=255, null=True, blank=True)
    Address = models.CharField(max_length=255, null=True, blank=True)
    City = models.CharField(max_length=255, null=True, blank=True)
    Region = models.CharField(max_length=255, null=True, blank=True)
    PostalCode = models.CharField(max_length=50, null=True, blank=True)
    Country = models.CharField(max_length=255, null=True, blank=True)
    Phone = models.CharField(max_length=50, null=True, blank=True)
    Fax = models.CharField(max_length=50, null=True, blank=True)
    HomePage = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.CompanyName

class Products(models.Model):
    ProductID = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=255)
    Supplier = models.ForeignKey(Suppliers, on_delete=models.CASCADE)
    Category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    QuantityPerUnit = models.CharField(max_length=255, null=True, blank=True)
    OldPrice = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    UnitPrice = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    UnitsInStock = models.IntegerField(null=True, blank=True, default=0)
    UnitsOnOrder = models.IntegerField(null=True, blank=True, default=0)
    ReorderLevel = models.IntegerField(null=True, blank=True, default=0)
    Discontinued = models.BooleanField(default=False)

    @property
    def discount_percentage(self):
        if self.OldPrice and self.UnitPrice and self.OldPrice > self.UnitPrice:
            return int(((self.OldPrice - self.UnitPrice) / self.OldPrice) * 100)
        return 0

    def __str__(self):
        return self.ProductName
