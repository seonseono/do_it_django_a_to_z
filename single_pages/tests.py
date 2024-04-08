from django.test import TestCase, Client
from django.contrib.auth.models import User
from bs4 import BeautifulSoup
from blog.models import Post

# Create your tests here.
class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_nina = User.objects.create_user(username='nina', password='somepassword')

    def test_landing(self):
        post_001 = Post.objects.create(
            title='1st Post',
            content='This is a 1st post',
            author=self.user_nina,
        )

        post_002 = Post.objects.create(
            title='2nd Post',
            content='This is a 2nd post',
            author=self.user_nina,
        )

        post_003 = Post.objects.create(
            title='3rd Post',
            content='This is a 3rd post',
            author=self.user_nina,
        )

        post_004 = Post.objects.create(
            title='4th Post',
            content='This is a 4th post',
            author=self.user_nina,
        )

        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')

        body = soup.body
        self.assertNotIn(post_001.title, body.text)
        self.assertIn(post_002.title, body.text)
        self.assertIn(post_003.title, body.text)
        self.assertIn(post_004.title, body.text)

# Create your tests here.
