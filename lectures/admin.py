from django.contrib import admin

from .models import *

class AdminStudentStage(admin.ModelAdmin):
    list_display = ('stage',)

class AdminLectures(admin.ModelAdmin):
    list_display = ('id', 'name', 'stage')
    search_fields = ('name',)
    list_filter = ('stage',)

class AdminLessons(admin.ModelAdmin):
    list_display = ('title', 'uploaded')
    search_fields = ('title',)
    list_filter = ('lectures',)


admin.site.register(StudentStage, AdminStudentStage)
admin.site.register(Lectures, AdminLectures)
admin.site.register(Lessons, AdminLessons)