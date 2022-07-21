from django.shortcuts import render, redirect
from .models import Post
from .form import AddPost

def index(request):
    post = Post.objects.all().order_by('-date')
    post_tag = Post.objects.filter()[:8]
    content = {
        'post':post,
        'cat':post_tag
    }
    return render(request, 'event/index.html', content)

def upload_post(request):
    if request.method == "POST":
        form = AddPost(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = AddPost()

    context = {'form':form}
    return render(request, 'event/upload.html', context)

def category(request, cats):
    post_tag = Post.objects.filter()[:8]
    category_post = Post.objects.filter(category=cats)
    return render(request, 'event/category.html', {'cats':cats, 'category':category_post, 'cat':post_tag})

def detail(request, pk):
    post_tag = Post.objects.filter()[:8]
    post = Post.objects.get(id=pk)
    context = {
        'post':post,
        'cat':post_tag
    }
    return render(request, 'event/detail.html', context)

def update(request, pk):
   post = Post.objects.get(id=pk)
   if request.method == "POST":
        form = AddPost(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("home")
   else:
    form = AddPost(instance=post)

    context = {'form':form}
    return render(request, 'event/upload.html', context)

def delete_message(request, pk):
    todo = Post.objects.get(id=pk)
    return render(request, 'event/delete.html', {'todo':todo})

def delete(request, pk):
   todo = Post.objects.get(id=pk)
   todo.delete()
   return redirect('home')

def search(request):
    post_tag = Post.objects.filter()[:8]
    if request.method == "POST":
        search = request.POST['searched']
        post = Post.objects.filter(title__contains=search)
        return render(request, 'event/search.html', {'post':post, 'search':search,'cat':post_tag})
    else:
        return render(request, 'event/search.html', {'cat':post_tag})