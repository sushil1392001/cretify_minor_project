from django.views import View
from django.shortcuts import render, redirect
from store.models.categories import Categories
from store.models.products import Products
from store.models.save import Save
import os


class Post(View):
    def get(self, request):
        categories = Categories.get_all_categories()
        customer = request.session.get('customer_id')
        products = Products.get_products_by_customerid(customer)
        save_product = request.GET.get('save')
        if save_product is not None:
            save_list = Save.get_save_product_of_customer(customer)
            product_id = []
            for i in save_list:
                product_id.append(i.save_product_id)
            products = Products.objects.filter(id__in=product_id)
        data = {
            'categories': categories,
            'email': request.session.get('email'),
            'products': products,
            'save': save_product
        }
        return render(request, 'post.html', data)

    def post(self, request):
        product_id = request.POST.get('product_id')
        if request.POST.get('delete'):
            product = Products.objects.filter(id=product_id)
            # delete the image in the upload/product folder
            file_name = product[0].image
            os.remove('uploads/' + str(file_name))

            # delete the image form data base
            product.delete()
        else:
            save = Save.objects.filter(save_product_id=product_id)
            save.delete()
            return redirect("http://127.0.0.1:8000/post?save=bookmark")
        return redirect('post')
