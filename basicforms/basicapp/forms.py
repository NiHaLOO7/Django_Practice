from multiprocessing.sharedctypes import Value
from django import forms
from django.core import validators

def check_for_letter(value):
    if value[0].lower() == 'z':
        raise forms.ValidationError("THE VALUE SHOULD NOT START WITH THE LETTER Z")

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_letter])
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter your Email again")
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])

    
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        if email != vmail:
            raise forms.ValidationError("The Emails don't match")
    
    ### Either this or validator.. validator is always a better option
    ###################################################################
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("Bot Alert")
    #     return botcatcher
