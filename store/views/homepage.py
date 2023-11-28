from django.views import View
from django.shortcuts import render, redirect
from store.models.categories import Categories
from store.models.products import Products
from store.models.customer import Customer
from store.models.save import Save
from store.models.like import Like


class Homepage(View):
    def get(self, request):
        categories = Categories.get_all_categories()
        categoriesid = request.GET.get('categories')
        search_str = request.GET.get('search')
        customer_id = request.session.get('customer_id')

        if search_str is not None:
            products = Products.get_products_by_titile_name(search_str)

        elif categoriesid:
            products = Products.get_all_products_by_categoryid(categoriesid)

        else:
            products = Products.get_all_products()

        get_bookmark_product = Save.get_save_product_of_customer(customer_id)
        get_like_product = Like.get_like_product_of_customer(customer_id)

        data = {
            'products': products,
            'categories': categories,
            'email': request.session.get('email'),
            'customer': Customer.objects.all(),
            'get_bookmark_product': get_bookmark_product,
            'get_like_product': get_like_product
        }
        cart = request.session.get('cart')
        if not cart:
            request.session.cart = {}
        return render(request, 'homepage.html', data)

    def post(self, request):
        bookmark_product_id = request.POST.get("bookmark")
        like_product_id = request.POST.get('like')
        productid = request.POST.get('productid')

        customer_id = request.session.get('customer_id')
        if bookmark_product_id is not None and customer_id is not None:
            if len(Save.check_product_already_save(customer_id, bookmark_product_id)) == 0:
                bookmark = Save(save_product_id=bookmark_product_id, save_customer_id=customer_id)
                bookmark.save()
            else:
                save = Save.objects.filter(save_product_id=bookmark_product_id)
                save.delete()

        if like_product_id is not None and customer_id is not None:
            if len(Like.check_product_already_like(customer_id, like_product_id)) == 0:
                likes = Like(like_product_id=like_product_id, lke_customer_id=customer_id)
                likes.save()
            else:
                like = Like.objects.filter(like_product_id=like_product_id)
                like.delete()

        cart = request.session.get('cart')
        if productid:
            cart = request.session.get('cart')
            if cart:
                cart[productid] = 1
            else:
                cart = {}
                cart[productid] = 1
        request.session['cart'] = cart
        return redirect('homepage')
