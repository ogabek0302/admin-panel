# from django.contrib import admin
# from .models import Category, Brand, Snakers

# class SnakersAdmin(admin.ModelAdmin):
#     list_display = ['model_name', 'color', 'price', 'brand', 'category']
#     search_field = ['name', 'price', 'brand']
#     list_filter = ['price', 'category']

# admin.site.register(Snakers, SnakersAdmin)
    

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name','created_at', 'updated_at']
#     search_fields = ['name']
#     list_filter = ['created_at']
    
#     def book_count(self, obj):
#         return str(len(obj.books.all()))+"ta"


# admin.site.register(Category, CategoryAdmin)

from django.contrib import admin
from .models import Category, Brand, Snakers, File

admin.site.site_header = 'Sneakers.uz'      # Header text
admin.site.index_title = 'Administration'    # Title on index page
admin.site.site_title = 'Our book world'     # Title in browser tab

admin.site.site_url = None   # Remove the "View site" link
admin.site.site_footer = '© 2023 Sneakers.uz'      # Footer text
admin.site.disable_action_group = True     # Disable the "Action" dropdown
admin.site.empty_value_display = '**Empty**'   # Customized display for empty values

class SnakersAdmin(admin.ModelAdmin):
    list_display = ['model_name', 'color', 'price', 'brand', 'category']
    search_field = ['name', 'price', 'brand']
    list_filter = ['price', 'category']
admin.site.register(Snakers, SnakersAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','created_at', 'updated_at']
    search_fields = ['name']
    list_filter = ['created_at']
    def book_count(self, obj):
        return str(len(obj.books.all()))+"ta"
admin.site.register(Category, CategoryAdmin)

class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    search_fields = ['name']
    list_filter = ['created_at']
admin.site.register(Brand, BrandAdmin)

class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_image', 'date_created', 'date_updated')
    list_filter = ('date_created', 'date_updated')
    
    def get_image(self, obj):
        return obj.image.url if obj.image else None
    get_image.short_description = 'Image'

admin.site.register(File, FileAdmin)