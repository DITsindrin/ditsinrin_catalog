from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify
from django.conf import settings
from django.core.mail import send_mail

from blog.models import Article


# Create your views here.

class ArticleListView(ListView):
    model = Article
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs) -> dict[str,]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'OnlineStore NewS'
        return context

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publication_sign=True)
        return queryset


class ArticleDetailView(DetailView):
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
            send_mail(
                subject='Просмотры статьи',
                message=f'Поздравляю! Просмотры статьи {self.object.title} достигли {self.object.views_count} просмотров!',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['dmitriytsindrin@mail.ru'],
            )

        return self.object


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'content', 'category', 'preview', 'publication_sign',)
    success_url = reverse_lazy('blog:blogs')

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            new_article.save()

        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'content', 'category', 'preview', 'publication_sign',)
    # success_url = reverse_lazy('blog:blogs')

    def get_success_url(self):
        return reverse('blog:blogs', args=[self.kwargs.get('pk')])


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog:blogs')
