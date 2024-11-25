from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('name',)

    def __str__(self):
        return str(self.name) # name 필드 값으로 표시
