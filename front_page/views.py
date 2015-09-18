from django.shortcuts import render
from django.views.generic.list import ListView
from front_page.models import Author,Blog,Catagory
from django.views.generic.detail import DetailView
# Create your views here.

def index(request):
    return render(request,'home.html',{})

class blog_home(ListView):
    paginate_by = 3
    model= Blog
    context_object_name = 'blog_title'
    template_name = 'blog.html'
    
    def get_context_data(self, **kwargs):
        context = super(blog_home,self).get_context_data(**kwargs)
        context['catagories'] = Catagory.objects.all()
        return context
        
class blog_search(ListView):
    paginate_by = 4
    context_object_name = 'blog_title'
    template_name = 'blog.html'
    
    def get(self, request, *args, **kwargs):
        if 'query' in request.GET:
            self.query = request.GET['query']
        return ListView.get(self, request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(blog_search,self).get_context_data(**kwargs)
        context['catagories'] = Catagory.objects.all()
        return context
    
    def get_queryset(self):
        if 'query' in self.kwargs:
            self.search_result = Blog.objects.filter(catagory__name = self.kwargs['query'])
        elif self.query:
            self.search_result = Blog.objects.filter(title__contains = self.query)
        return self.search_result
    
class blog_post(DetailView):
    model = Blog
    context_object_name = 'title'
    template_name = 'blog_post.html'