from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


# Create your views here.

def base(request):
    return render(request, 'base.html', )


def home(request):
    search = request.GET.get('search')
    if search:
        items = ListItem.objects.filter(title__icontains=search)
    else:
        items = ListItem.objects.all()
    return render(request, 'home.html', locals())


def add_list(request):
    if request.method == 'POST':
        items = ListItem()
        items.title = request.POST.get('title')
        items.description = request.POST.get('description')
        messages.success(request, 'An item has been added on list')
        items.save()
        return redirect('home')
    return render(request, 'add_list.html', )


def update(request, id):
    items = ListItem.objects.get(id=id)
    if request.method == 'POST':
        items.title = request.POST.get('title')
        items.description = request.POST.get('description')
        items.save()
        messages.success(request, 'List is updated')
        return redirect('home')

    return render(request, 'add_list.html', locals())


def delete(request, id):
    items = ListItem.objects.get(id=id)
    items.delete()
    messages.success(request, 'One item is deleted')

    return redirect('home')


def insideItem(request, id):
    items = ListItem.objects.get(id=id)
    return render(request, 'inside_item.html', locals())


def complete(request, id):
    items = ListItem.objects.get(id=id)
    items.status = True
    items.save()
    return redirect('home')


def incomplete(request, id):
    items = ListItem.objects.get(id=id)
    items.status = False
    items.save()
    return redirect('home')
