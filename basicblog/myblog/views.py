from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, UpdatePostForm
from django.urls import reverse_lazy

# def home(request):
#     return render(request, 'home.html', {})


class HomeView(ListView):  # Home page
    model = Post
    template_name = 'home.html'
    ordering = ['-id']


class ContactView(ListView):  # contact page
    model = Post
    template_name = 'contact.html'


class ArticleDetailView(DetailView):  # blog post detail page
    model = Post
    template_name = "article_details.html"


class AddPostView(CreateView):  # add blog post form page
    model = Post  # using post model imported from models/post
    form_class = PostForm  # using my own post form imported from models/forms
    template_name = 'add_post.html'  # using the add_post.html file
    # fields = '__all__'


class UpdatePostView(UpdateView):  # update blog post form page
    model = Post  # using post model imported from models/post
    template_name = 'update_post.html'  # using the add_post.html file
    # fields = ['title', 'title_tag', 'body']
    form_class = UpdatePostForm


class DeletePostView(DeleteView):  # Delete blog post form page
    model = Post  # using post model imported from models/post
    template_name = 'delete_post.html'  # using the add_post.html file
    success_url = reverse_lazy('home')
    # fields = '__all__'
    # form_class = UpdatePostForm
