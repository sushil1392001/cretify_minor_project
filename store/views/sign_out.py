from django.views import View
from django.shortcuts import render, redirect


class Sign_out(View):
    def get(self, request):
        request.session.clear()
        return redirect('homepage')
