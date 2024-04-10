from django.contrib import admin
from .models import coaches, trainees, News, Sports

# Register your models here.
class  CoachesAdmin(admin.ModelAdmin):
    list_display = ['name', 'nationality', 'role']
    search_fields = ['name','nationality']
    list_filter = ['role', 'nationality']
    
admin.site.register(coaches, CoachesAdmin)

admin.site.register(trainees)

admin.site.register(News)

admin.site.register(Sports)