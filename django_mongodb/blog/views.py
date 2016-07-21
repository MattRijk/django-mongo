# Create your views here.
from django.shortcuts import render_to_response
from blog.models import Post

def home(request):
    post = Post.objects.all()
    return render_to_response('blog/home.html', {'object_list': post})