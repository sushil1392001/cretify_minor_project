# from django.conf import settings
# from django.conf.urls.static import static
from django.urls import path
from store.views.homepage import Homepage
from store.views.sign_up import Sign_up
from store.views.sign_in import Sign_in
from store.views.sign_out import Sign_out
from store.views.otp import Otp
from store.views.post import Post
from store.views.add import Add
from store.views.about import About
from store.views.contact import Contact
from message.views.chat import Chat
from store.views.cart import Cart
from store.middleware.auth import auth_middleware

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('sign-up', Sign_up.as_view(), name='signup'),
    path('sign-in', Sign_in.as_view(), name='signin'),
    path('sign-out', Sign_out.as_view(), name='signout'),
    path('post', auth_middleware(Post.as_view()), name='post'),
    path('add', auth_middleware(Add.as_view()), name='add'),
    path('otp', Otp.as_view(), name='otp'),
    path('chat', Chat.as_view(), name='chat'),
    path('about', About.as_view(), name='about'),
    path('contact', Contact.as_view(), name='contact'),
    path('cart', Cart.as_view(),name='cart')
]
