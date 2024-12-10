from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from utils.decorators import log_files
from utils.common import inject_image
from .models import Item
from .forms import NewItemForm, EditItemForm

# Create your views here.


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(
        category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html', {
        'item': inject_image(item),
        'related_items': related_items
    })


@login_required
@log_files
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            # create an object but not save it before adding 'created_by' field
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()  # now save it

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Add new item',
    })


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')


@login_required
@log_files
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    # form의 인자로 instance(item)를 전달함으로써 수정 작업을 수행함.

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES,
                            instance=item)

        if form.is_valid():
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item',
        'pk': item.id
    })


def category(request, category_id):
    items = Item.objects.filter(category=category_id, is_sold=False)

    return render(request, 'item/category.html', {
        'items': list(map(inject_image, items))
    })
