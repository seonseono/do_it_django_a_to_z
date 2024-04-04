from django.db import models
from django.contrib.auth.models import User
import os

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'

    class Meta:
        verbose_name_plural = 'Categories'


class Post(models.Model):
    title = models.CharField(max_length=30) # Title field
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField() # Content field

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d', # 폴더를 만들어서 주소로 이미지 가져옴
                                   blank=True) # 이미지 공백 허용(이미지 첨부하지 않아도 작동함)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d',
                                   blank=True) # 마찬가지로 파일 첨부 생략 가능 옵션
    created_at = models.DateTimeField(auto_now_add=True) # 처음 레코드가 생성된 시점을 자동으로 입력
    update_at = models.DateTimeField(auto_now=True) # 레코드가 가장 마지막으로 저장된 시점(수정된 시점)
    # author field
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    # category field
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}] {self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name) # 파일명만 나오게 하는 함수

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1] # 파일 이름을 split해서 맨 뒤의 확장자만 반환

