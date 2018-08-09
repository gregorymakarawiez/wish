from django import forms
from django.contrib.auth.forms import AuthenticationForm 
from .models import Unit, Employee
from django.contrib.auth.models import User
from parsley.decorators import parsleyfy


class SigninForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, required=True,
                               widget=forms.TextInput(attrs={'type':'text', 'name': 'username', 'placeholder':'User name','class':'form-control'}))
    password = forms.CharField(label="Password", max_length=30, required=True,
                               widget=forms.TextInput(attrs={'type':'password', 'name': 'password', 'placeholder':'Password','class':'form-control'}))










@parsleyfy
class SignupForm(forms.Form):

    class Meta:
        parsley_extras={
            'text_input_debug':{
                'minlength':"2",
                'error-msg': 'This value is too short. It should be at least 2 characters long.'
            }
        }

    text_input_debug = forms.CharField(
        label="debug",
        min_length=2,
        max_length=5,
        required=True,
        widget=forms.TextInput(
            attrs={
                'type':'text',
                'name': 'text_input_debug',
                'placeholder':'text input debug...',
                'class':'form-control',
            }
        ),
        error_messages = {
            'min_length': 'This value length is false. It should be between 2 and 5 characters long.',
            'max_length': '',
            'required': 'Do not forget to provide a first name',
         },
    )

    first_name = forms.CharField(
        label="First name",
        min_length=3,
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'name': 'first_name',
                'placeholder': 'First name',
                'class': 'form-control has-feedback-left'
            }
        ),
        error_messages = {
            'min_length': 'length should be greater or equal to 3',
            'max_length': 'length should be smaller or equal to 30',
            'required': 'Do not forget to provide a first name',
        },
    )

    last_name = forms.CharField(
        label="Last name",
        min_length=3,
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'name': 'last_name',
                'placeholder': 'Last name',
                'class': 'form-control has-feedback-right'
            }
        ),
        error_messages = {
            'min_length': 'length should be greater or equal to 3',
            'max_length': 'length should be smaller or equal to 30',
            'required': 'Do not forget to provide a first name',
            },
    )

    username = forms.CharField(
        label="Username",
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                'type':'text',
                'name': 'username',
                'placeholder':'User name',
                'class': 'form-control',
            }
        )
    )

    password = forms.CharField(
        label="Password",
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                'type':'password',
                'name': 'password',
                'placeholder':'Password',
                'class':'form-control'
            }
        )
    )

    email = forms.CharField(
        label="Email",
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                'type':'email',
                'name': 'email',
                'placeholder':'Email',
                'class':'form-control'
            }
        )
    )



    unit = forms.ModelChoiceField(
        queryset=Unit.objects.all(),
        required=True,
        widget=forms.Select(
            attrs={
                'name': 'unit',
                'class': 'form-control'
            }
        )
    )

    manager = forms.ModelChoiceField(
        queryset=Employee.objects.filter(is_manager=True),
        required=False,
        widget=forms.Select(
            attrs={
                'name': 'manager',
                'class': 'form-control'
            }
        )
    )

    is_manager=forms.BooleanField(
        label="I manage a team",
        required=False,
        initial=False,
        widget=forms.CheckboxInput(
            attrs={
                'name': 'is_manager'
            }
        )
    )

    is_continuous_improvement_officer=forms.BooleanField(
        label="I manage continous improvement",
        required=False,
        initial=False,
        widget=forms.CheckboxInput(
            attrs={
                'name': 'is_continuous_improvement_officer'
            }
        )
    )


    subscribed_to_newsletter = forms.BooleanField(
        label="Subscribe to newsletter",
        required=False,
        initial=False,
        widget=forms.CheckboxInput(
            attrs={
                'name': 'subscribed_to_newsletter'
            }
        )
    )





    def clean_username(self):
        qs = User.objects.filter(username=self.cleaned_data['username'])

        if qs.count():
            print("clean_username error #############################")
            raise forms.ValidationError(
                'That username is already in use')
        else:
             return self.cleaned_data['username']


    def clean_email(self):
        qs = User.objects.filter(email=self.cleaned_data['email'])
        if qs.count():
            print("clean_username error #############################")
            raise forms.ValidationError(
                'That email is already in use')
        else:
             return self.cleaned_data['email']
