from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator
from django.forms import inlineformset_factory
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from online_store.forms import ProductForm, ProductUpdateForm, VersionForm
from online_store.models import Product, Contacts, CategoryProduct, ProductVersion


# Create your views here.

@login_required
def home(request):
    """Контроллер главной страницы"""
    title = 'OnlineStore'
    greetings = 'Добро пожаловать на сайт самого дружелюбного маркетплейса. У нас Вы можете купить необходимую технику и почитать наши технические блоги'
    context = {
        'title': title,
        'appeal': greetings,

    }
    return render(request, 'online_store/home.html', context)


@login_required
def contacts(request):
    """Контроллер страницы с контактами"""
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


class ProductListView(LoginRequiredMixin, ListView):
    """Контроллер страницы со списком продуктов"""
    model = Product
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Популярные продукты'
        # context['version'] = self.object_list.subject_set.all().filter(version_flag=True)

        queryset = super().get_queryset()
        for product in queryset:
            version = product.productversion_set.filter(version_flag=True)
            context['version'] = version
            print(context['version'])

        return context


class ProductDetailView(LoginRequiredMixin, DetailView):
    """Контроллер страницы с детальной информацией о продукте"""
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Контроллер страницы создания продукта"""
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('online_store:products')
    permission_required = 'online_store.add_product'

    # def form_valid(self, form):
    #     self.object = form.save()
    #     self.object.user = self.request.user
    #     self.object.save()
    #
    #     return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, ProductVersion, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST)
        else:
            context_data['formset'] = VersionFormset()

        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        self.object.user = self.request.user
        self.object.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер страницы изменения продукта"""
    model = Product
    form_class = ProductUpdateForm
    success_url = reverse_lazy('online_store:products')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user == self.request.user or self.object.user.is_staff == True:
            return self.object
        else:
            raise Http404

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, ProductVersion, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Контроллер страницы удаления продукта"""
    model = Product
    success_url = reverse_lazy('online_store:products')
    permission_required = 'online_store.delete_product'


# FBV (function based views)
# def products(request):
#     product = Product.objects.all()
#
#     paginator = Paginator(product, 4)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     title = 'Популярные продукты'
#
#     context = {
#         'products': product,
#         'title': title,
#         'page_obj': page_obj,
#     }
#
#     return render(request, 'online_store/product_list.html', context)


# def product_detail(request, pk):
#     try:
#         product_id = Product.objects.get(pk=pk)
#     except Product.DoesNotExist:
#         raise Http404("Book does not exist")
#
#     context = {
#         'product_id': product_id,
#         'product': Product.objects.filter(id=pk),
#         'title': product_id.title,
#     }
#     print(context)
#
#     return render(request, 'online_store/product_detail.html', context)


# def product_create(request):
#     new_product = Product()
#     category_product = CategoryProduct.objects.all()
#     if request.method == "POST":
#         new_product.title = request.POST.get("title")
#         new_product.category = category_product.get(id=int(request.POST.get("category")))
#         new_product.price = request.POST.get("price")
#         print(new_product)
#         new_product.save()
#         return redirect('online_store:products')
#
#     return render(request, 'online_store/product_form.html')

@login_required
def base_test(request):
    """Для тестов"""
    title = 'OnlineStore'
    greetings = 'Добро пожаловать на сайт самого дружелюбного маркетплейса. У нас Вы можете купить необходимую технику и почитать наши технические блоги'
    context = {
        'title': title,
        'appeal': greetings,

    }
    return render(request, 'online_store/base_test.html', context)
