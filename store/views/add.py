from django.views import View
from django.shortcuts import render, redirect
from store.models.categories import Categories
from store.models.products import Products
from store.models.customer import Customer
from store.models.form import Add_form


class Add(View):
    def get(self, request):
        categories = Categories.get_all_categories()
        form = Add_form()

        data = {
            'categories': categories,
            'email': request.session.get('email'),
            'form': form,
        }
        return render(request, 'add.html', data)

    def post(self, request):
        form = Add_form(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.customer_id = request.session.get('customer_id')
            obj.save()
            return redirect('post')
        else:
            return redirect('add')
