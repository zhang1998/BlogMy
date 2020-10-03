from django.db import models
from django.utils  import timezone
from django.contrib.auth.models  import User

# Create your models here.
# 和文件上传对应的内容

class article(models.Model):
    #title
    title=models.CharField(max_length=300)
    #content
    author=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="blog_posts")
    #user
    body=models.TextField()
    #
    publish=models.DateTimeField(default=timezone.now)
    #
    class Meta:
        ordering=("-publish",)#规定了实例对象的显示顺序 即按照publish的字段进行显示

    def __str__(self):
        return self.title
