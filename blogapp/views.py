from django.shortcuts import render, redirect
from .models import BlogPost
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
# def create(request):
#     return render(request,'create.html')
def list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'list.html', {'posts': posts})
@login_required(login_url="login")
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        # author = request.POST.get('author')
        author=request.user
        image = request.FILES.get('image')

        BlogPost.objects.create(title=title, content=content, author=author, image=image)
        return redirect('list')

    return render(request, 'create.html', {'post': None})

def delete(request,pk):
    instance = BlogPost.objects.get(pk=pk)
    instance.delete()
    return redirect('list')
def edit(request, pk):
    post =  BlogPost.objects.get(pk=pk)

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.author = request.POST.get('author')
        if request.FILES.get('image'):
            post.image = request.FILES.get('image')
        post.save()
        return redirect('list')

    return render(request, 'create.html', {'post': post})
def view(request,pk):
    post =  BlogPost.objects.get(pk=pk)
    return render(request, 'view.html', {'post': post})



# def edit(request):
#     return render(request,'edit.html')
