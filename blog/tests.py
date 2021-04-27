from time import timezone

from django.contrib.auth.models import User
from django.test import TestCase

from blog.models import Post, Comment


class PostTestCases(TestCase):
    def setUp(self):
        self.author = User.objects.create_user(username="testuser", password="12345")
        Post.objects.create(
            title="Test title",
            slug="test-title",
            author=self.author,
            body="Post content",
            status="published",
        )

    def test_storing_post(self):
        """Test if post data are stored properly."""

        post = Post.objects.get(title="Test title")

        self.assertEqual(post.title, "Test title")
        self.assertEqual(post.slug, "test-title")
        self.assertEqual(post.author, self.author)
        self.assertEqual(post.body, "Post content")


class CommentsTestCases(TestCase):
    def setUp(self):
        self.author = User.objects.create_user(username="testuser", password="12345")
        self.post = Post.objects.create(
            title="Test title",
            slug="test-title",
            author=self.author,
            body="Post content",
            status="published",
        )
        Comment.objects.create(
            post=self.post,
            name="Mateusz",
            email="testemail@gmail.com",
            body="Comment content",
        )

    def test_storing_post(self):
        """Test if post data are stored properly."""

        comment = Comment.objects.get(post=self.post)

        self.assertEqual(comment.post, self.post)
        self.assertEqual(comment.name, "Mateusz")
        self.assertEqual(comment.email, "testemail@gmail.com")
        self.assertEqual(comment.body, "Comment content")
