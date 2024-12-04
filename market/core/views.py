from django.shortcuts import render, redirect
from django.contrib import messages

from item.models import Category, Item
from .forms import SignupForm

def index(request):
    print(messages.get_messages(request))
    items = Item.objects.filter(is_sold=False) [0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            messages.success(request, f"Welcome, {user.username}! Your account has been created.")
            return redirect('/login/')
        
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })
    
def login(request):
    return render(request, 'core/login.html')