from django.contrib import admin
from .models import Musician,Album,Product,Post
# Register your models here.

# class BlogAdminArea(admin.AdminSite):
#      site_header = 'tneyba Blog'


# blog_site=BlogAdminArea(name='BlogAdmin')



class MusicianModelAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','instrument')
    list_display_links=['first_name']
    list_filter=['first_name', 'last_name','instrument']
    search_fields=['first_name']
    class Meta:
        model = Musician
        
class AlbumModelAdmin(admin.ModelAdmin):
    list_display = ('artist', 'name','release_date')
    class Meta:
        model = Album
 
 
        
admin.site.register(Musician,MusicianModelAdmin)
admin.site.register(Album,AlbumModelAdmin)


admin.site.register(Product)
admin.site.register(Post)
