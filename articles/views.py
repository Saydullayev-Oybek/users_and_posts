from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from articles.models import Article

# Create your views here.


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleCreateView(LoginRequiredMixin, UserPassesTestMixin ,CreateView):
    model = Article
    template_name = 'article_create.html'
    fields = ('title', 'body', 'summary', 'photo')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser

class ArticleUpdateView(UserPassesTestMixin ,LoginRequiredMixin ,UpdateView):
    model = Article
    template_name = 'article_edit.html'
    fields = ('title', 'body', 'summary', 'photo')
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(UserPassesTestMixin ,LoginRequiredMixin ,DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

