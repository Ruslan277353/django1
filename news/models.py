from django.db import models


from django.db import models

class NewsCategory(models.Model):
    category_name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class NewsModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to='new_images')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'

class MyUserModel(models.Model):
    username = models.CharField(max_length=60)
    email = models.EmailField()
    phone_number = models.IntegerField()
    password = models.CharField(max_length=120)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'MyUser'
        verbose_name_plural = 'MyUsers'