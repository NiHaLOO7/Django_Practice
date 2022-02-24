from django import forms
from appTwo.models import User

class NewUserForm(forms.ModelForm):
    ###### custom validation here
    # first_name = forms.CharField(validators=[check_for_letter])
    class Meta():         # class Meta:   is also correct
        model = User
        fields = '__all__'
