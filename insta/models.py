from django.db import models

from django.contrib.auth.models import User
 
class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    image = models.ImageField(upload_to="posts/")

    caption = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
 
    def total_likes(self):

        return self.like_set.count()
 
    def __str__(self):

        return f"{self.user.username} Post"
 
 
class Like(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
 
 
class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
 
 
class Follow(models.Model):

    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")

    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")

 
