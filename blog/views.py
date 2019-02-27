from django.shortcuts import render,get_object_or_404
from .models import Blog
from django.views.generic import DetailView

# Create your views here.
def blog_list(request):
    queryset = Blog.objects.all()

    context = {
        'blogs': queryset,
    }
    return render(request,'blog/blog.html',context)


class Blog_detail(DetailView):
    model = Blog
    template_name= 'blog/blog-single.html'


# def blog_detail(request,id):
#     # queryset = Blog.objects.all(id=pk)
#     queryset = get_object_or_404(Blog,pk=id)

#     context = {
#         'blog': queryset
#     }

#     return render(request,'blog/blog-single.html',context)


