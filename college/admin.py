from django.contrib import admin
from .models import Problem,Comment,SubComment,Contact,Deta
from .models import Image,Hostel,Mess_timetable,Entry
# Register your models here.

# class Problem(admin.ModelAdmin):
#     list_display=('name')
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','photo']

admin.site.register(Problem)
admin.site.register(Comment)
admin.site.register(SubComment)
admin.site.register(Contact)
admin.site.register(Deta)
admin.site.register(Hostel)
admin.site.register(Mess_timetable)
admin.site.register(Entry)
