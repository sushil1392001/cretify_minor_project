from django.core.mail import send_mail
from django.views import View
from django.shortcuts import render, redirect
from store.models.categories import Categories
from store.models.customer import Customer
import re
from django.contrib.auth.hashers import make_password
import random


class Sign_up(View):
    def get(self, request):
        categories = Categories.get_all_categories()
        return render(request, 'sign_up.html', {'categories': categories})

    def post(self, request):
        error_message = None
        categories = Categories.get_all_categories()
        # get the email and password
        username = request.POST.get('Username')
        email = request.POST.get('Email')
        password = request.POST.get('password')

        # create the object of customer:
        customer = Customer(username=username, email=email, password=password)
        # validation:

        if not re.search(r"^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@gmail.com", email):
            error_message = 'Invalid Email'

        if len(password) < 8:
            error_message = "Minimum password length should be 8 characters."
        # check already signup or not form this email
        if customer.isExists():
            error_message = 'This email has already been used to register.'

        if customer.username_isexits():
            error_message = 'This username already exists.'

        if not error_message:
            # password hashing
            customer.password = make_password(customer.password)

            # save customer detail
            customer.register()

            request.session['customer_id'] = customer.id
            request.session['email'] = customer.email
            request.session['username'] = customer.username

            return redirect('homepage')

            # return redirect('otp',)

        else:
            return render(request, 'sign_up.html', {'error': error_message, 'categories': categories})
