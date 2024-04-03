from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post

# Create your tests here.
class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_post_list(self):
        response = self.client.get('/blog/')
        self.assertEquals(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEquals(soup.title.text, 'Blog')
        navbar = soup.nav
        self.assertIn('Blog', navbar.text)
        self.assertIn('About Me', navbar.text)

        self.assertEquals(Post.objects.count(), 0)
        main_area = soup.find('div', id='main-area')
        self.assertIn('Not yet to post', main_area.text)

        post_001 = Post.objects.create(
            title='1st Post',
            content='Hello World. We are the world',
        )
        post_002 = Post.objects.create(
            title='2nd Post',
            content='1등이 전부는 아니잖아요?',
        )
        self.assertEquals(Post.objects.count(), 2)

        response = self.client.get('/blog/')
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEquals(response.status_code, 200)

        main_area = soup.find('div', id='main-area')
        self.assertIn(post_001.title, main_area.text)
        self.assertIn(post_002.title, main_area.text)

        self.assertNotIn('Not yet to post', main_area.text)