from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.
#메인페이지 : 자기소개 + 각 게시글 제목
def home(request) :
    posts = Post.objects
    return render(request, 'herokuApp/home.html', {'posts' : posts})

#게시글 제목 + 내용
def post(request):
    posts = Post.objects.all()
    return render(request, 'herokuApp/post.html', {'posts' : posts})

#글작성
def create(request) :
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('post')
    else :
        form = PostForm()
        return render(request, 'herokuApp/create.html', {'form' : form})

#수정하기
def edit(request, id) :
    post = get_object_or_404(Post, id = id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post', post.id)
    else :
        form = PostForm(instance=post)
    return render(request, 'edit.html', {'form':form}) 