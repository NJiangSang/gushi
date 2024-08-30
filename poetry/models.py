from django.db import models


class Poem(models.Model):
    title = models.CharField(max_length=100)  # 标题
    author = models.CharField(max_length=50)  # 作者
    type = models.CharField(max_length=50)  # 类型
    content = models.TextField()  # 内容
    image = models.ImageField(upload_to='images/', null=True, blank=True)  # 插图（可选）
    video_url = models.URLField(null=True, blank=True)  # 视频链接（可选）
    is_deleted = models.IntegerField(default=0)  # 确保这一行正确

    def __str__(self):
        return self.title
