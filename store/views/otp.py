import random
from django.core.mail import send_mail
from django.views import View
from django.shortcuts import render, redirect
from store.models.categories import Categories
from store.models.customer import Customer
import re


class Otp(View):
    def get(self, request):
        otp = random.randrange(1000, 1000000)
        email = request.session.get('email')
        print('********************',email,otp)
        send_mail(
            "Verify your Email",
            f"Your OTP is {otp}",
            "devil1392001@gmail.com",
            [email],
            fail_silently=False,

        )
        return render(request, 'otp_page.html',{'email':email})
