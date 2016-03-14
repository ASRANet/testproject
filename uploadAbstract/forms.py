from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)
from uploadAbstract.models import SubmittedAbstract


class UserForm(forms.ModelForm):
    salutation = forms.ChoiceField(choices=(("Mr.", "Mr."), ("Mrs.", "Mrs."), ("Ms.", "Ms."), ("Dr.", "Dr."),
                                            ("Prof.", "Prof."), ("Sir", "Sir"), ("Lady", "Lady"), ("Lord", "Lord")),
                                   required=True)
    primary_author_first_name = forms.CharField(max_length=35)
    primary_author_surname = forms.CharField(max_length=35)
    co_authors_names = forms.CharField(max_length=770, required=False, help_text="Separate each author with a comma")
    email = forms.EmailField(max_length=60, required=True)
    paper_title = forms.CharField(max_length=60, required=True)
    abstract = forms.CharField(max_length=2000, required=True, widget=forms.Textarea)

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('/uploadAbstract/', 'Upload Abstract', css_class='btn-primary'))

    class Meta:
        model = SubmittedAbstract
        fields = ('salutation', 'primary_author_first_name', 'primary_author_surname',
                  'co_authors_names', 'email', 'paper_title', 'abstract')
