from django.db import models

# Create your models here.
# انواع کوئری ها
# https://docs.djangoproject.com/en/3.2/topics/db/queries/

# آموزش کار با aggrigate , annotate
# https://docs.djangoproject.com/en/3.1/topics/db/aggregation/

# مثال های manytomany
# https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_many/

from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline