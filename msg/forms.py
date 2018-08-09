from django import forms
from .widgets import MyQuillWidget4



class EditForm(forms.Form):
    message = forms.CharField(
        #label="my message",
        widget=MyQuillWidget4,
    #message = forms.CharField()
    )


