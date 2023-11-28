from django.db import models
from .categories import Categories
from .customer import Customer
import datetime


class Products(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, default=1)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, default="", null=True, blank=True)
    image = models.ImageField(upload_to='products')
    datetime = models.DateTimeField(default=datetime.datetime.now())

    @staticmethod
    # it serve all the products
    def get_all_products():
        return Products.objects.all()

    @staticmethod
    # it serve the all product related to this  categoryid
    def get_all_products_by_categoryid(category_id=None):
        if category_id:
            return Products.objects.filter(category=category_id)
        else:
            return Products.objects.all()

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter(
            id__in=ids)  # it give all the detail about the product and (id__in) means we pass the list of products id

    @staticmethod
    def get_products_by_customerid(customer_id):
        return Products.objects.filter(customer=customer_id)

    @staticmethod
    def get_products_by_titile_name(string):
        customer = Customer.objects.filter(username__icontains=string)
        if len(customer) != 0:
            product = Products.objects.filter(customer=customer[0])
        else:
            product = Products.objects.filter(name__icontains=string)
        return product
