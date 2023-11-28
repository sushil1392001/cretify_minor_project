from django import template
from store.models.like import Like

register = template.Library()


@register.filter(name='username')
def username(product, customer):
    for i in customer:
        if product.customer_id == i.id:
            return i.username


@register.filter(name='change_bookmark_icon')
def change_bookmark_icon(product, get_bookmark_product):
    for i in get_bookmark_product:
        if int(i.save_product_id) == int(product.id):
            return True


@register.filter(name='change_like_icon')
def change_like_icon(product, get_like_product):
    for i in get_like_product:
        if i.like_product_id == int(product.id):
            return True

@register.filter(name='count_likes')
def count_likes(product):
    return len(Like.objects.filter(like_product_id=int(product.id)))


