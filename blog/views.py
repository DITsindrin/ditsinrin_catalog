from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify
from django.conf import settings
from django.core.mail import send_mail

from blog.models import Article
from blog.services import get_category_article_cache


# Create your views here.

class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    paginate_by = 8
    category_list_cache = get_category_article_cache()

    def get_context_data(self, *, object_list=None, **kwargs) -> dict[str,]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'OnlineStore NewS'
        context['category_list'] = self.category_list_cache

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(publication_sign=True)
        return queryset


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article

    def get_context_data(self, **kwargs) -> dict[str,]:
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()

        if self.object.views_count == 100:
            test = send_mail(
                subject='Просмотры статьи',
                message=f'Поздравляю! Просмотры статьи {self.object.title} достигли {self.object.views_count} просмотров!',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['ditsindrin@yandex.ru'],
            )
            print(test)
        return self.object


class ArticleCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Article
    fields = ('title', 'content', 'category', 'preview', 'publication_sign',)
    success_url = reverse_lazy('blog:blogs')
    permission_required = 'blog.add_article'

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            new_article.save()

        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Article
    fields = ('title', 'content', 'category', 'preview', 'publication_sign',)
    permission_required = 'blog.change_article'

    # success_url = reverse_lazy('blog:blogs')

    def get_success_url(self):
        return reverse('blog:blogs')


class ArticleDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('blog:blogs')
    permission_required = 'blog.delete_article'
