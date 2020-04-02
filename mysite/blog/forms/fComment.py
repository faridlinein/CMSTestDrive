from django import forms
from blog.models import Comment

"""NOTE_START 
Remember that Django has two base classes to build forms, Form and ModelForm
To create a form from a model, we will just need to indicate which
model to use to build the form in the Meta class of the form. Django
introspects the model and builds the form dynamically for us. Each
model field type has a corresponding default form field type.. 
NOTE_END""" 
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
