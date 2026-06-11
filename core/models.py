from django.db import models
from django.contrib.auth.models import User

class blogs(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    content=models.TextField()
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
 