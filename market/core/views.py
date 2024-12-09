from django.shortcuts import render, redirect
from django.contrib import messages

from utils.decorators import log_headers
from utils.common import inject_image
from item.models import Category, Item
from .forms import SignupForm, LoginForm


@log_headers
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': list(map(inject_image, items)),
    })


def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            messages.success(
                request, f"Welcome, {user.username}! Your account has been created.")
            return redirect('/login/')

    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })


def login(request):
    form = LoginForm()

    return render(request, 'core/login.html', {
        'form': form
    })
