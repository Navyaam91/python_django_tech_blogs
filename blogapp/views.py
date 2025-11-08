from django.shortcuts import render, redirect
from .models import BlogPost
import pprint


# Create your views here.
# def create(request):
#     return render(request,'create.html')
def list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'list.html', {'posts': posts})

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        content = request.POST.get('content')

        # Save to database
        BlogPost.objects.create(title=title, author=author, content=content)

        # Redirect to homepage or post list after saving
        return redirect('list')   # make sure 'home' is defined in urls.py
    return render(request, 'create.html')
def delete(request,pk):
    instance = BlogPost.objects.get(pk=pk)
    instance.delete()
    return redirect('list')
def edit(request,pk):
    post=BlogPost.objects.get(pk=pk)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.author = request.POST.get('author')
        post.save()
        return redirect('list')
    return render(request, 'create.html',{'post':post})

# def edit(request):
#     return render(request,'edit.html')
