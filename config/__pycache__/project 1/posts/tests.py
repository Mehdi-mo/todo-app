from django.test import TestCase
from django.urls import reverse
from .models import Post
from django.contrib.auth.models import User

class PostsListViewTest(TestCase): 
    def test_posts_list_view_url(self):
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)

    def test_post_list_view_url_by_name(self):
        response = self.client.get(reverse('posts:list'))
        self.assertEqual(response.status_code, 200)

    def test_post_list_page(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        Post.objects.create(
            title='test-post',
            body='test post is here',
            slug='test-post-slug',
            author=user
            )
            
        
        response = self.client.get(reverse('posts:list'))
        self.assertContains(response,'test post is here')