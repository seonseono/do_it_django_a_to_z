# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    ordering = '-pk' # 이 옵션이 없으면 post1부터 정렬됨
    # template_name = 'blog/post_list.html'
    # CBV 사용 시 템플릿 이름 강제 지정

class PostDetail(DetailView):
    model = Post


# def index(request):
#     posts = Post.objects.all().order_by('-pk') # 역순 정렬(나중에 올린 글부터)
#     return render(request,
#               'blog/post_list.html',
#               {
#                   'posts':posts,
#               })


# def single_post_page(request, pk):
#     # 하나의 게시물만 가져옴 기본키값=입력받은 기본키값
#     post = Post.objects.get(pk=pk)
#     return render(request,
#                   'blog/post_detail.html',
#                   {
#                       'post' : post,
#                   })

