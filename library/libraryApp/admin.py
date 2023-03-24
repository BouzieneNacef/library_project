from django.contrib import admin

# Register your models here.
from.models import*

class BookAdmin(admin.ModelAdmin):
    list_display=("title","price","nbPages",)

admin.site.register(Book,BookAdmin)
admin.site.register(Editor)
admin.site.register(Author)
admin.site.register(Addres)