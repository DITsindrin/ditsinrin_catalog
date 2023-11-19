from django.shortcuts import render

from online_store.models import Product, Contacts


# Create your views here.


def home(request):
    products = Product.objects.order_by('-id')

    print(products[:5])
    return render(request, 'online_store/home.html')


def contacts(request):
    contact = Contacts.objects.all()
    print(contact)

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}{phone}{message}')
    return render(request, 'online_store/contacts.html', {'contact': contact})
