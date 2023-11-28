from django.views import View
from django.shortcuts import render, redirect
from store.models.categories import Categories
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password


class Sign_in(View):
    def get(self, request):
        categories = Categories.get_all_categories()
        return render(request, 'sign_in.html', {'categories': categories})

    def post(self, request):
        error_message = None
        categories = Categories.get_all_categories()

        # get the email and password
        email = request.POST.get('Email')
        password = request.POST.get('password')

        customer = Customer.get_customer_by_email(email=email)
        if customer and check_password(password, customer.password):
            # create the session
            request.session['customer_id'] = customer.id
            request.session['email'] = customer.email
            request.session['username'] = customer.username
            return redirect('homepage')
        else:
            error_message = 'Email or Password invalid !!'
        return render(request, 'sign_in.html', {'error': error_message, 'categories': categories})
