from django.contrib import admin

from .models import Question, Choice

"""NOTE_START 
One small problem, though. It takes a lot of screen space to display all 
the fields for entering related Choice objects. For that reason, Django offers 
a tabular way of displaying inline related objects. To use it, change the 
ChoiceInline declaration to read:
NOTE_END""" 
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]

    # list_display = ('question_text', 'pub_date')
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)

"""NOTE_START 
There are two ways to solve this problem. The first is to register Choice with 
the admin just as we did with Question

But, really, this is an inefficient way of adding Choice objects to the system.
It’d be better if you could add a bunch of Choices directly when you create 
the Question object. Let’s make that happen.
NOTE_END""" 
