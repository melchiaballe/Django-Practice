from django.contrib import admin

# Register your models here.
from .models import Question, Choice

#admin.site.register(Question)
admin.site.register(Choice)

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']
    fieldsets = (
        (None, {
            "fields": (
                ['question_text']
            ),
        }),
        ('Date information', {
            "fields":(
                ['pub_date']
            )
        })
    )
    inlines = [ChoiceInLine]

    

admin.site.register(Question, QuestionAdmin)