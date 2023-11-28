from django.views import View
from django.shortcuts import render, redirect
from store.models.categories import Categories


class Contact(View):
    def get(self, request):
        categories = Categories.get_all_categories()
        data={
            'email': request.session.get('email'),
            "categories":categories
        }
        return render(request, "contact.html", data)
