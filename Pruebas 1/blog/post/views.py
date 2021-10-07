from django.shortcuts import render , get_object_or_404 , redirect
from .models import Post
from .forms import PostForm
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request , 'post/post_list_index.html' , {'posts':posts})

def post_details(request , pk):
    post = get_object_or_404(Post , pk=pk)
    return render(request , 'post/post_details.html' , {'post':post})

def post_form(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            return redirect('post_details' , pk=post.pk)
    else:
        form = PostForm()
    return render(request , 'post/post_form.html' , {'form' : form})