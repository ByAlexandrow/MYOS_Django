from django import forms
from tinymce.widgets import TinyMCE

from texts.models import (
    Texts
)


class TextsForm(forms.ModelForm):
    texts_description = forms.CharField(
        widget=TinyMCE(
            attrs={
                'cols': 20,
                'rows': 20
            }
        )
    )
    text = forms.CharField(
        widget=TinyMCE(
            attrs={
                'cols': 80,
                'rows': 30
            }
        )
    )

    class Meta:
        model = Texts
        fields = ['texts_description', 'text']