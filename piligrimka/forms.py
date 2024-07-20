from django import forms
from tinymce.widgets import TinyMCE

from piligrimka.models import Piligrimka


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
        model = Piligrimka
        fields = ['our_story']