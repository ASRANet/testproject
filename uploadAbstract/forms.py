from django import forms
from uploadAbstract.models import SubmittedAbstract


class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=40, help_text="First Name", required=True)
    last_name = forms.CharField(max_length=40, help_text="Last Name", required=True)
    email = forms.EmailField(max_length=60, help_text="Email Address", required=True)
    abstract = forms.CharField(max_length=2000, help_text="Abstract", required=False, widget=forms.Textarea)
    #feeNormal = forms.CharField(max_length=60, help_text="I wish to register for the conference at the normal price of " +
    #                                                    chr(156) + "450", required=True)

    class Meta:
        model = SubmittedAbstract
        fields = ('first_name', 'last_name', 'email', 'abstract')
