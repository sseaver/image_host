from django.shortcuts import render
from app.models import Category, Profile, Comment, Post
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy


class IndexView(ListView):
    template_name = "index.html"
    model = Post
    paginate_by = 6

    def get_context_data(self):
        context = super().get_context_data()
        context['login_form'] = AuthenticationForm
        return context


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'description', 'image', 'categories')
    success_url = reverse_lazy('profile_view')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.created_by = self.request.user
        return super().form_valid(form)


class PostDetailCommentCreateView(CreateView):
    model = Comment
    fields = ('content',)
    template_name = 'app/post_detail_comment_create.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailCommentCreateView, self).get_context_data(**kwargs)
        context['post'] = Post.objects.get(id=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.created_by = self.request.user
        instance.relation_post = Post.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        post_id = self.kwargs['pk']
        return "/post/{}/".format(post_id)


class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'description', 'image', 'categories')
    success_url = reverse_lazy('profile_view')


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('profile_view')


class CommentUpdateView(UpdateView):
    model = Comment
    fields = ('content',)
    success_url = reverse_lazy('post_detail_comment_create_view')


class ProfileView(ListView):
    template_name = "profile.html"
    model = Post

    def get_queryset(self):
        return Post.objects.filter(created_by=self.request.user)
