'''
from django.test import TestCase
from newsite.blog.models import Post
from django.contrib.auth.models import User
from django.utils import timezone



class PostTestCase(TestCase):

    def setUp(self):
        # Set up non-modified objects used by all test methods
        self.author = User.objects.create(username='Test')
        self.post = Post.objects.create(
            author=self.author,
            title='First Test',
            text='Content Test',
            created_date=timezone.now(),
            published_date=timezone.now())

    def test_title(self):
        self.assertEqual(self.post.title, 'First Test')

    def test_username(self):
        self.assertEqual(self.post.author, self.author)

'''