from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.
#상속페이지
def layout(request):
    return render(request, 'herokuApp/layout.html')

#메인페이지
def main(request):
    posts = Post.objects
    return render(request, 'herokuApp/main.html', {'posts':posts})

#글쓰기 페이지
def new(request):
    return render(request, 'herokuApp/new.html')

#글쓰기 함수
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.pubdate = timezone.now()
            form.save()
            return redirect('main')
    else:
        form = PostForm()
        return render(request, 'herokuApp/new.html', {'form':form})