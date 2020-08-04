from django.contrib import admin
from p_library.models import Book, Author, Publisher
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name

    list_display = ('title', 'author_full_name', 'publisher',)
    fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'publisher', 'price', 'copy_count',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    #@staticmethod
    #def author_full_name(obj):
        #return obj.full_name
    #list_display = ('author_full_name',) - так тоже работает

    list_display = ('full_name',)
    fields = ('full_name', 'birth_year', 'country')

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name',)
