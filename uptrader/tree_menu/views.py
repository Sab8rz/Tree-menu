from django.shortcuts import render


def home(request):
    return render(request, 'tree_menu/home.html')


def main_menu(request):
    return render(request, 'tree_menu/home.html')

def secondary_menu(request):
    return render(request, 'tree_menu/home.html')

def about(request):
    return render(request, 'tree_menu/home.html')


def products(request):
    return render(request, 'tree_menu/home.html')


def phones(request):
    return render(request, 'tree_menu/home.html')


def laptops(request):
    return render(request, 'tree_menu/home.html')


def info(request):
    return render(request, 'tree_menu/home.html')


def faq(request):
    return render(request, 'tree_menu/home.html')


def contacts(request):
    return render(request, 'tree_menu/home.html')