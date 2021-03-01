from django.db import models

# Create your models here.


class summary(models.Model):
    date = models.DateTimeField(auto_now=True)
    text = models.TextField()

    def __str__(self):
        return self.text
