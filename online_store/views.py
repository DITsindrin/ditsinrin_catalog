from django.core.paginator import Paginator
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect

from online_store.models import Product, Contacts, CategoryProduct
from .forms import ProductForm


# Create your views here.


def home(request):
    title = 'OnlineStore'
    greetings = 'Добро пожаловать на сайт самого дружелюбного маркетплейса. У нас Вы можете купить необходимую технику и почитать наши технические блоги'
    context = {
        'title': title,
        'appeal': greetings,

    }
    return render(request, 'online_store/home.html', context)


def contacts(request):
    contact = Contacts.objects.all()
    title = 'Наши контакты'
    support = 'Можете заполнить Ваши данные и отправить вопрос. Мы свяжемся с Вами в ближайшее время.'
    context = {
        'contact': contact,
        'title': title,
        'appeal': support,
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

    return render(request, 'online_store/contacts.html', context)


def products(request):
    product = Product.objects.all()

    paginator = Paginator(product, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    title = 'Популярные продукты'

    context = {
        'products': product,
        'title': title,
        'page_obj': page_obj,
    }

    return render(request, 'online_store/product_list.html', context)


def product_detail(request, pk):
    try:
        product_id = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        raise Http404("Book does not exist")

    context = {
        'product_id': product_id,
        'product': Product.objects.filter(id=pk),
        'title': product_id.title,
    }
    print(context)

    return render(request, 'online_store/product_detail.html', context)


def product_create(request):
    new_product = Product()
    category_product = CategoryProduct.objects.all()
    if request.method == "POST":
        new_product.title = request.POST.get("title")
        new_product.category = category_product.get(id=int(request.POST.get("category")))
        new_product.price = request.POST.get("price")
        print(new_product)
        new_product.save()
        return redirect('online_store:products')

    return render(request, 'online_store/product_create.html')


def base_test(request):
    title = 'OnlineStore'
    greetings = 'Добро пожаловать на сайт самого дружелюбного маркетплейса. У нас Вы можете купить необходимую технику и почитать наши технические блоги'
    context = {
        'title': title,
        'appeal': greetings,

    }
    return render(request, 'online_store/base_test.html', context)
