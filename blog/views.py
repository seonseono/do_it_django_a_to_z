from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Category, Tag


class PostCreate(CreateView):
    model = Post
    fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category']

class PostList(ListView):
    model = Post
    ordering = '-pk' # 이 옵션이 없으면 post1부터 정렬됨
    # template_name = 'blog/post_list.html'
    # CBV 사용 시 템플릿 이름 강제 지정

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

def category_page(request, slug):
    if slug == 'no_category':
        category = 'Unclassified'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    return render(
        request,
        'blog/post_list.html',
        {
            'post_list' : post_list,
            'categories' : Category.objects.all(),
            'no_category_post_count' : Post.objects.filter(category=None).count(),
            'category' : category,
        }
    )

def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()

    return render(
        request,
        'blog/post_list.html',
        {
            'post_list' : post_list,
            'tag' : tag,
            'categories' : Category.objects.all(),
            'no_category_post_count' : Post.objects.filter(category=None).count(),
        }
    )



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

