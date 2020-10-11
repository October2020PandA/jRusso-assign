from django.contrib import admin

# Register your models here.
from questionTaker.models import Answer, CompleteGroup
class AnsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Answer, AnsAdmin)
class CompGroupAdmin(admin.ModelAdmin):
    pass
admin.site.register(CompleteGroup, CompGroupAdmin)
