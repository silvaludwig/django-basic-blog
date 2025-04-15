from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm


# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):  # Home page
    model = Post
    template_name = 'home.html'


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
