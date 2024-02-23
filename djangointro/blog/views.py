from django.shortcuts import render
from .models import blog
# Create your views here.
def view_blogs (request):
    blogs = Blog.objects.all()
    context = {"blogs":blogs}
    return render(request,"blog/index.html", context)