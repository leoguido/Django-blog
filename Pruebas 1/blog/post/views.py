from django.http import request
from django.shortcuts import render , get_object_or_404 , redirect
from .models import Post , Comment
from .forms import PostForm , CommentForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request , 'post/post_list_index.html' , {'posts':posts})

def post_details(request , pk):
    post = get_object_or_404(Post , pk=pk)
    return render(request , 'post/post_details.html' , {'post':post})

@login_required
def post_form(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('post_details' , pk=post.pk)
    else:
        form = PostForm()
    return render(request , 'post/post_form.html' , {'form' : form})

@login_required
def post_edit(request , pk):
    post = get_object_or_404(Post , pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST , instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('post_details' , pk=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request , 'post/post_edit.html' , {'form':form})

@login_required
def post_draft_list(request):
    post = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request , 'post/post_draft_list.html' , {'post': post})

@login_required
def post_publish(request , pk):
    post = get_object_or_404(Post , pk=pk)
    post.publish()
    return redirect('post_details' , pk=post.pk)

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post , pk=pk)
    post.delete()
    return redirect('post_list')

def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)        
        if form.is_valid():            
            comment = form.save(commit=False)            
            comment.post = post            
            comment.save()            
            return redirect('post_details', pk=post.pk)    
    else:        
        form = CommentForm()    
        return render(request, 'post/add_comment_to_post.html', {'form': form})

@login_required
def remove_comment(request , pk):
    comment = get_object_or_404(Comment, pk=pk)    
    comment.delete()    
    return redirect('post_details', pk=comment.post.pk)

@login_required
def approve_comment(request , pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve_comment()    
    return redirect('post_details', pk=comment.post.pk)