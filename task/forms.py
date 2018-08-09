from django import forms
from .models import Task
from account.models import Employee, Unit
import datetime
from Wish.widgets import QuillWidget,  DatePickerWidget
import json
from Wish import settings
from django.forms.utils import ErrorDict






class CreateForm(forms.Form):


    headline = forms.CharField(
        error_messages={'required':'Please provide a headline'},
        label="Headline",
        max_length=30,
        required=True,
        widget=forms.Textarea(
            attrs={
                'type': 'text',
                'name': 'headline',
                'placeholder': 'Short description',
                'rows': '1',
                'class': 'form-control has-feedback-left',
                'style': 'resize:none;'
            }
        ),
    )

    problem = forms.CharField(
        label="Problem",
        max_length=1000,
        required=False,
        widget=QuillWidget(
            attrs={
                'placeholder': 'Short description',
            }
        ),
    )

    proposal = forms.CharField(
        error_messages={'required': 'Please provide your proposal'},
        label="Proposal",
        max_length=1000,
        required=True,
        widget=QuillWidget(
            attrs={
                'placeholder': 'Short description',
                'class': 'form-control has-feedback-left',
            }
        ),
    )

    validator = forms.ModelChoiceField(
        error_messages={'required': 'Please provide a validator'},
        label="Validator",
        queryset=Employee.objects.filter(is_manager=True),
        required=True,
        widget=forms.Select(
            attrs={
                'name': 'validator',
                'class': 'form-control'
            }
        )
    )

    def clean_headline(self):

        headline=self.cleaned_data['headline']

        if headline:
            # check if this headline is already registered
            qs = Task.objects.filter(headline=headline)

            if qs.exists():
                #raise forms.ValidationError(
                #    {'headline': 'Sorry, that headline is already in use, please forward another one'})
                raise forms.ValidationError(
                    'Sorry, that headline is already in use, please forward another one')
        return headline



    def clean_proposal(self):
        proposal = self.cleaned_data['proposal']

        proposal_jsn=json.loads(proposal)
        print(proposal_jsn)
        insert_txt=proposal_jsn['ops'][0]['insert']
        print("proposal: %s" % proposal)
        print("insert_txt: %s" % insert_txt)
        if insert_txt == "\n":
             print("raise exception")
             raise forms.ValidationError(
                'Please, submit here your proposal')

        return proposal

    """
    def clean_proposal(self):
        proposal = self.cleaned_data['proposal']

        print("proposal:")
        print(proposal)
        if proposal:
            content=json.loads(proposal)
        else:
            content={}
        content=content['ops'][0]['insert']

        if content=="\n":
            # check if a proposal has been submitted

            #raise forms.ValidationError(
            #    {'proposal': 'Please, submit here your proposal'})
            raise forms.ValidationError(
                'Please, submit here your proposal')
        return proposal
    """

class EditForm(CreateForm):

    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)
        self.fields["headline"].widget.attrs['readonly']= True


    def clean_headline(self):
        headline = self.cleaned_data['headline']

        return headline




class ValidateForm(forms.Form):


    CHOICES=(('1','Waiting for validation'),('2','Accepted'),('5','Refused'))


    validation_choice = forms.ChoiceField(
        widget=forms.RadioSelect(
            attrs={
                'type': 'radio',
                'class': 'flat',
            }
        ),
        choices=CHOICES
    )


    validation_text = forms.CharField(
        label="Comment",
        max_length=1000,
        required=False,
        widget=QuillWidget(
            attrs={
                'placeholder': 'Short description',
                'class': 'form-control has-feedback-left',
            }
        ),
    )

    task_due_date = forms.DateField(
        #input_formats=settings.DATE_INPUT_FORMATS,
        label="Task completion",
        required=True,
        widget=DatePickerWidget()
    )

    standard_update_due_date = forms.DateField(
        #input_formats=settings.DATE_INPUT_FORMATS,
        label="Standard update",
        required=True,
        widget=DatePickerWidget(),
    )

    implementer = forms.ModelChoiceField(
        error_messages={'required': 'Please provide an implementer'},
        label="Implementer",
        #queryset=Employee.objects.filter(manager=self.actor), # list of manager employees
        queryset=Employee.objects, # list of manager employees
        required=True,
        validators=[],
        widget=forms.Select(
            attrs={
                'name': 'implementer',
                'class': 'form-control'
            }
        )
    )

    mailing_list = forms.ModelChoiceField(
        label="Mailing list",
        queryset=Unit.objects,  # list of units
        required=False,
        validators=[],
        widget=forms.Select(
            attrs={
                'name': 'validator',
                'class': 'form-control'
            }
        )
    )
    """
    def clean_standard_update_due_date(self):
        print(self.cleaned_data)
        standard_update_due_date = self.cleaned_data['standard_update_due_date']

        if not standard_update_due_date:
            raise forms.ValidationError(
                'Please provide the date at which standard must be updated')
        return standard_update_due_date

    def clean_task_due_date(self):
        print(self.cleaned_data)
        task_due_date = self.cleaned_data['task_due_date']

        if not task_due_date:
            raise forms.ValidationError(
                'Please provide the due date')
        return task_due_date
    """


class SubmitForm(forms.Form):

    approver = forms.ModelChoiceField(
        error_messages={'required': 'Please provide an approver'},
        label="Approver",
        queryset=Employee.objects.filter(is_manager=True),
        required=True,
        widget=forms.Select(
            attrs={
                'name': 'approver',
                'class': 'form-control'
            }
        )
    )



class ApproveForm(forms.Form):


    approved = forms.BooleanField(
        label="I Approve",
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'js-switch',
                'type': 'checkbox'
            }
        )
    )

