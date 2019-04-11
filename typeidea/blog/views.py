from django.db.models import Q # 实现搜索功能
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post, Tag, Category
from config.models import SideBar
from django.views.generic import ListView, DetailView

# Create your views here.


class CommentViewMixin:
    def get_context_data(self, **kwargs):
        context = self.get_context_data(**kwargs)
        context.update({
            'sidebars': SideBar.get_all(),
        })
        context.update(Category.get_navs())
        return context


class IndexView(ListView):
    queryset = Post.latest_posts()
    paginate_by = 5
    context_object_name = 'post_list'
    template_name = "blog/list.html"


class CategoryView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        category = get_object_or_404(Category, pk=category_id)
        context.update({
            'category': category,
        })
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category__id=category_id)


class TagView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_id = self.kwargs.get('tag_id')
        tag = get_object_or_404(Tag, pk=tag_id)
        context.update({
            'tag': tag,
        })
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        tag_id = self.kwargs.get('tag_id')
        return queryset.filter(tag__id=tag_id)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'


class PostListView(DetailView):
    queryset = Post.latest_posts()
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'

class SearchView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update({
            'keyword': self.request.GET.get('keyword', '')
        })
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        keyword = self.request.GET.get('keyword')
        if not keyword:
            return queryset
        # 相当于SELECT * FROM post WHERE title ILIKE '%<keyword>%' or desc ILIKE '%<keyword>%'
        return queryset.filter(Q(title__icontains=keyword) | Q(desc__icontains=keyword))
