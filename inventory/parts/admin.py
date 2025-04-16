from django.contrib import admin
from django.urls import reverse
from .models import Part, PartCategory

# Register your models here.

@admin.register(PartCategory)
class PartCategoriesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name',]
    search_help_text = 'Search by name'
    
    

@admin.register(Part)
class PartsAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'part_number')
    list_filter = ('type',)
    list_select_related = ('type',)
    search_fields = ['name', 'part_number']
    search_help_text = 'Search by name or part number'
    autocomplete_fields = ['type']
    fieldsets = (
        ('Part Details', {
            'fields': ('type', 'name', 'part_number')
        }),
        ('Stock and Prices', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('stock_quantity', 'selling_price', 'break_even_price')
        }),
        ('Other Details', {
            'fields': ('description',)
        }),
    )
    
    def view_on_site(self, obj):
        url = reverse('parts:detail', kwargs={'pk': obj.pk})
        return url
    
    