from django.db import models

# class BlogAuthorProfile(models.Model):
#     name = models.CharField(max_length=100, null=True, blank=True)
#     bio = models.TextField(blank=True)
#     email = models.EmailField(unique=True)

#     def __str__(self):
#         return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    # author = models.ForeignKey(BlogAuthorProfile, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# class BlogDetails(models.Model):
#     post = models.OneToOneField(BlogPost, on_delete=models.CASCADE, related_name='details')
#     seo_title = models.CharField(max_length=255, blank=True)
#     views = models.IntegerField(default=0)
#     read_time = models.PositiveIntegerField(help_text="Estimated reading time in minutes", default=1)


