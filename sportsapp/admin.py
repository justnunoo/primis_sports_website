from django.contrib import admin
from .models import Coaches, Trainees, News, Sports

# Register your models here.
class  CoachesAdmin(admin.ModelAdmin):
    list_display = ['name', 'nationality', 'role']
    search_fields = ['name','nationality']
    list_filter = ['role', 'nationality']
    
admin.site.register(Coaches, CoachesAdmin)

admin.site.register(Trainees)

admin.site.register(News)

admin.site.register(Sports)