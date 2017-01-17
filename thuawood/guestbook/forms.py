from django import forms
from .models import Entry


class Form(forms.ModelForm):

    class Meta:
        model = Entry
        exclude = ('create_date', 'homepage')

    spamcheck = forms.CharField(max_length=len('stockholm'), required=True,
                                label="Sveriges huvudstad?",
                                help_text="For att få bort spam robottar")

    def clean_spamcheck(self):
        value = self.cleaned_data['spamcheck']
        if value.strip().lower() != 'stockholm':
            raise forms.ValidationError('Är du en människa eller en robot?')
        return value
