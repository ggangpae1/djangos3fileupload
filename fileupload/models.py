from django.db import models

class FileUpload(models.Model):
    title = models.TextField(max_length=40, null=True)
    #파일의 자료형은 ImageField로 설정
    imgfile = models.ImageField(null=True, upload_to="", blank=True)
    content = models.TextField()

    def __str__(self):
        return self.title
