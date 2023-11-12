from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'online_store/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}{phone}{message}')
    return render(request, 'online_store/contacts.html')