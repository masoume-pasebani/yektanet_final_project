from django.contrib import admin

# Register your models here.
from Interview.models import Interview, Comment, Feedback

admin.site.register(Interview)
admin.site.register(Comment)
# admin.site.register(Feedback)