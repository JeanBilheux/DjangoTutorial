from django.contrib import admin
from .models import Book, Author

#this is to personalize the way the admin page looks

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Book Detail", {"fields": ["title", "authors"]}),
        ("Review", {"fields": ["is_favorite", "review", "date_reviewed"]}),
    ]
    
    readonly_fields = ("date_reviewed",)
    
    # to have a many_to_many field in the table
    def book_authors(self, obj):
        return obj.list_authors()
    
    # to change the label of the columns
    book_authors.short_description = "Author (s)"
    
    # list of columns to display
    list_display = ("title", "book_authors", "date_reviewed", "is_favorite", "review",)

    # to be able to edit fields from the table itself
    list_editable = ("is_favorite", "date_reviewed",)

    # to order the books by the following columns
    list_display_links = ("title",)

    # create favorites
    list_filter = ("is_favorite",)

    # to give option to search fields
    search_fields = ("title", "authors__name",)
    

#admin.site.register(Book, BookAdmin)
admin.site.register(Author)
