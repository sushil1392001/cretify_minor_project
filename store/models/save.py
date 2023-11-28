from django.db import models


class Save(models.Model):
    save_product_id = models.CharField(max_length=30)
    save_customer_id = models.CharField(max_length=30)

    @staticmethod
    def get_save_product_of_customer(customer_id):
        return Save.objects.filter(save_customer_id=customer_id)
    @staticmethod
    def check_product_already_save(customer_id,product_id):
        return Save.objects.filter(save_customer_id=customer_id,save_product_id=product_id)