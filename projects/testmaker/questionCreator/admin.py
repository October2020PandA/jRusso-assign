from django.contrib import admin

# Register your models here.
from questionCreator.models import QuestionType, QuestionGroup
class QTAdmin(admin.ModelAdmin):
    pass
admin.site.register(QuestionType, QTAdmin)
class QGAdmin(admin.ModelAdmin):
    pass
admin.site.register(QuestionGroup, QGAdmin)