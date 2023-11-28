from django.db import models


class Like(models.Model):
    like_product_id = models.IntegerField()
    lke_customer_id = models.IntegerField()
    counter = models.IntegerField(default=0)

    @staticmethod
    def check_product_already_like(customer_id, product_id):
        return Like.objects.filter(lke_customer_id=customer_id, like_product_id=product_id)

    @staticmethod
    def get_like_product_of_customer(customer_id):
        return Like.objects.filter(lke_customer_id=customer_id)

