from django import forms
from django.core import validators

def check_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("NAME NEEDS TO START Z")

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label = 'Enter your email again: ')
    text = forms.CharField(widget = forms.Textarea)
    # bot_catcher = forms.CharField(required=False, widget=forms.HiddenInput,
    # )

    # def cleaned_botcatcher(self):
    #     bot_catcher = self.cleaned_data['bot_catcher']
    #     if len(bot_catcher) > 0:
    #         raise forms.ValidationError("GOTCHA BOT!")
    #     return bot_catcher

    def clean(self):
        all_data = super().clean()
        email = all_data['email']
        vmail = all_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Emails don't match!")
