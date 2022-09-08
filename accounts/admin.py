from django.contrib import admin

# Register your models here.
from accounts.models import Applicant, Interviewer, HR

admin.site.register(Applicant)
admin.site.register(Interviewer)
admin.site.register(HR)