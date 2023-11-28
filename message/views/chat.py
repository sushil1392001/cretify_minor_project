from django.views import View
from django.shortcuts import render, redirect
from store.models.categories import Categories


class Chat(View):
    def get(self, request):
        categories = Categories.get_all_categories()
        return render(request, "chat.html", {'categories': categories,'email': request.session.get('email'),})

