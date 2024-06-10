from django import forms
from tinymce.widgets import TinyMCE

from victoria.models import Victoria


class TextsForm(forms.ModelForm):
    our_story = forms.CharField(
        widget=TinyMCE(
            attrs={
                'cols': 20,
                'rows': 20
            }
        )
    )

    class Meta:
        model = Victoria
        fields = ['our_story']
