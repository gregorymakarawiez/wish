from django import forms
from .models import Unit, Employee
from django.contrib.auth.models import User
from django.contrib.auth.password_validation  import validate_password
import re
from django.contrib.auth import authenticate, login



class SigninForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(SigninForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = ['username', 'password']


    username = forms.CharField(
        label="Username",
        max_length=30,
        required=True,
        error_messages={'required': 'Please provide your username'},
        widget=forms.TextInput(
            attrs={
                'type':'text',
                'name': 'username',
                'placeholder':'Donald',
            }
        )
    )

    password = forms.CharField(
        label="Password",
        max_length=30,
        required=True,
        error_messages={'required': 'Please provide your password'},
        widget=forms.TextInput(
            attrs={
                'type':'password',
                'name': 'password',
                'placeholder':'ThatsAllFolks',
                'class':'form-control'
            }
        )
    )


    def clean(self):

        # get field values
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username:
            # check if username is registered
            qs = User.objects.filter(username=username)

            if not qs.exists():
                raise forms.ValidationError(
                    {'username':'Sorry, that username is not registered'})

        if password:
            # check if password match with username
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError(
                    {'password':'Sorry, that password does not match given username'})

        # OK
        return self.cleaned_data





class SignupForm(forms.Form):

    first_name = forms.CharField(
        error_messages={'required':'Please provide your first name'},
        label="First name",
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'name': 'first_name',
                'placeholder': 'Donald',
                'class': 'form-control has-feedback-left'
            }
        ),
    )

    last_name = forms.CharField(
        error_messages={'required': 'Please provide your last name'},
        label="Last name",
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'name': 'last_name',
                'placeholder': 'McDuck',
                'class': 'form-control has-feedback-right'
            }
        ),
    )

    username = forms.CharField(
        error_messages={'required': 'Please provide your username'},
        label="Username",
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                'type':'text',
                'name': 'username',
                'placeholder':'donald',
            }
        )
    )

    password = forms.CharField(
        error_messages={'required': 'Please provide a password'},
        label="Password",
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                'type':'password',
                'name': 'password',
                'placeholder':'ThatsAllFolks',
                'class':'form-control'
            }
        )
    )

    email = forms.CharField(
        error_messages={'required': 'Please provide your email'},
        label="Email",
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                'type':'email',
                'name': 'email',
                'placeholder':'donald.mcduck@disney.com',
                'class':'form-control',
                #'pattern': "^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@disney[.]com$",
            }
        )
    )


    unit = forms.ModelChoiceField(
        error_messages={'required': 'Please provide your unit'},
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


    # check given username is unique (not already used by another employee)
    def clean_username(self):

        username = self.cleaned_data['username']


        if username:
            qs = User.objects.filter(username=username)

            if qs.exists():
                raise forms.ValidationError(
                    'Sorry, that username is already in use, please forward another one')

        return username


    # check complexity of given password using django utility functions
    def clean_password(self):

        new_password=(self.cleaned_data['password'])

        # use django contrib password validators, listed in setting.py|AUTH_PASSWORD_VALIDATORS
        # raise ValidationError if one of the validators fails
        validate_password(new_password)

        return self.cleaned_data['password']


    # check e-mail format and uniqueness
    def clean_email(self):

        # get posted email
        new_email=self.cleaned_data['email']

        # check email format + domain
        pattern=re.compile("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@disney[.]com$")
        if not pattern.match(new_email):
            raise forms.ValidationError(
                'Sorry, only @disney.com domain are authorized')

        # check that given  email is not already in use
        qs = User.objects.filter(email=new_email)
        if qs.exists():
            raise forms.ValidationError(
                'Sorry, that email is already in use, please forward another one')


        return self.cleaned_data['email']



'''class ProfileForm(forms.Form):

    def __init__(self, user, *args, **kwargs):

        # get instance of the employee that is editing his/her profile
        self.employee = Employee.objects.filter(user__pk=user.pk)[0]



    first_name = forms.CharField(
        label="First name",
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
    )

    last_name = forms.CharField(
        label="Last name",
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
                'placeholder':'donald.mcduck@disney.com',
                'class':'form-control',
                #'pattern': "^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@disney[.]com$",
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

        # get actual username
        actual_username=self.employee.user.username

        # get posted username
        new_username=self.cleaned_data['username']

        # if username unchanged, validate username
        if new_username == actual_username:
            return new_username

        # if username changed, check that it does not already exist in db
        qs = User.objects.filter(username=self.cleaned_data['username'])

        if qs.exists()():
            raise forms.ValidationError(
                'Sorry, that username is already in use, please forward another one')
        else:
             return self.cleaned_data['username']



    def clean_password(self):

        new_password=(self.cleaned_data['password'])

        # use django contrib password validators, listed in setting.py|AUTH_PASSWORD_VALIDATORS
        # raise ValidationError if one of the validators fails
        validate_password(new_password)

        return self.cleaned_data['password']


    def clean_email(self):

        # get actual email
        actual_email=self.employee.user.email

        # get posted email
        new_email=self.cleaned_data['email']

        # if email unchanged, validate email
        if new_email == actual_email:
            return email

        # check email format + domain
        pattern=re.compile("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@disney[.]com$")
        if not pattern.match(new_email):
            raise forms.ValidationError(
                'Sorry, only @disney.com domain are authorized')

        # check that given  email is not already in use
        qs = User.objects.filter(email=new_email)
        if qs.exists():
            raise forms.ValidationError(
                'Sorry, that email is already in use, please forward another one')


        return self.cleaned_data['email']
'''