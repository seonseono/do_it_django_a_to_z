from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30) # Title field
    content = models.TextField() # Content field

    created_at = models.DateTimeField(auto_now_add=True) # 처음 레코드가 생성된 시점을 자동으로 입력
    update_at = models.DateTimeField(auto_now=True) # 레코드가 가장 마지막으로 저장된 시점(수정된 시점)

    def __str__(self):
        return f'[{self.pk}] {self.title}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

