from django.db import models

# Create your models here.



#Abstract base classes¶
# https://docs.djangoproject.com/en/3.2/topics/db/models/#model-inheritance
class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    # step2
    class Meta:
        abstract = True
        ordering = ['name']

class Student(CommonInfo):
    home_group = models.CharField(max_length=5)
    
    #step2
    class Meta(CommonInfo.Meta):
        db_table = 'student_info'


# Multi-table inheritance
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)


# Proxy models¶
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class MyPerson(Person):
    class Meta:
        proxy = True

    # def do_something(self):
    #     # ...
    #     pass


# Multiple inheritance
# class Article(models.Model):
#     article_id = models.AutoField(primary_key=True)
#     # ...

# class Book(models.Model):
#     book_id = models.AutoField(primary_key=True)
#     # ...

# class BookReview(Book, Article):
#     pass


# or
class Piece(models.Model):
    pass

class Article(Piece):
    article_piece = models.OneToOneField(Piece, on_delete=models.CASCADE, parent_link=True)
    # ...

class Book(Piece):
    book_piece = models.OneToOneField(Piece, on_delete=models.CASCADE, parent_link=True)
    # ...

class BookReview(Book, Article):
    pass



class Artist(models.Model):
    name = models.CharField(max_length=10)

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.RESTRICT)   #test with models.CASCADE

# examples
    # >>> artist_one = Artist.objects.create(name='artist one')
    # >>> artist_two = Artist.objects.create(name='artist two')
    # >>> album_one = Album.objects.create(artist=artist_one)
    # >>> album_two = Album.objects.create(artist=artist_two)
    # >>> song_one = Song.objects.create(artist=artist_one, album=album_one)
    # >>> song_two = Song.objects.create(artist=artist_one, album=album_two)
    # >>> album_one.delete()
    # # Raises RestrictedError.
    # >>> artist_two.delete()
    # # Raises RestrictedError.
    # >>> artist_one.delete()
    # (4, {'Song': 2, 'Album': 1, 'Artist': 1})