from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import CreateForm, EditForm, ValidateForm, SubmitForm, ApproveForm
from account.models import Employee





@login_required
def list(request):
    tasks = Task.objects.order_by('creation_date')
    return render(request, 'list_tasks.html', {'tasks': tasks, 'state_choices':Task.state_choices} )


@login_required
def create(request):


    fields=['headline',
            'problem',
            'proposal',
            'validator']

    # get instance of the user that is editing his/her profile
    user = request.user

    # get instance of the employee that is creating the task
    employee = Employee.objects.filter(user__pk=user.pk)[0]


    if request.method == "POST":

        # if user strikes cancel, redirect to task list
        if request.POST.get("cancel"):
            return redirect('task:list')

        # handles form submitted by user
        form = CreateForm(request.POST)

        print("Create form is valid: %r" % form.is_valid() )

        if form.is_valid():

            # get data provided by user
            cleaned_data = form.cleaned_data

            # create new task
            task = Task()
            for field in fields:
                setattr(task, field, cleaned_data[field])

            # add automatic fields and save instance to db
            task.create(employee)

            # if everything goes well, redirect to task list
            return redirect("task:list")

    else:
        # delivers a blank form to be filled in
        form = CreateForm()


    # render form using given html template
    return render(request, 'create_task.html', {'form': form})





@login_required
def edit(request,pk, page):

    forms={'1': CreateForm,
           '2': ValidateForm}

    templates={'1': 'edit_task.html',
               '2': 'validate_task.html'}

    save_functions={'1': 'create',
                    '2': 'validate'}

    actors={'1': 'creator',
            '2': 'validator'}


    form=forms[page]
    template=templates[page]
    save_function=save_functions[page]
    actor=actors[page]
    fields=form.base_fields

    # get task instance
    task = get_object_or_404(Task, pk=pk)

    # get instance of the user whom the request is coming from
    user = request.user

    # get instance of corresponding employee
    employee = Employee.objects.filter(user__pk=user.pk)[0]

    # get task state
    state=task.state

    if request.method == "POST":

        # if user strikes cancel, redirect to task list
        if request.POST.get("cancel"):
            return redirect('task:list')

        # handles form submitted by user
        form = form(request.POST)

        if form.is_valid():

            # get data provided by user
            cleaned_data = form.cleaned_data

            # create new task
            for field in fields:
                setattr(task, field, cleaned_data[field])

            # add automatic fields and save instance to db, with the help of model saving methods (1 method by wizard page)
            save_function=getattr(task,save_function)
            save_function(employee)

            # if everything goes well, redirect to task list
            return redirect("task:list")

    else:

        # create context
        context={field: getattr(task,field) for field in fields}

        # delivers a blank form to be filled in
        form = form(context)


    # render form using given html template
    return render(request, template, {'form': form, 'page': state, 'pk': pk, 'state':state})




@login_required
def edit_wizard(request,pk, page):


    wizard_template='form_wizard.html'

    wizard_titles={'1': 'Propose',
                   '2': 'Validate',
                   '3': 'Submit',
                   '4': 'Approve'}

    forms={'1': EditForm,
           '2': ValidateForm,
           '3': SubmitForm,
           '4': ApproveForm}

    templates={'1': 'edit_task.html',
               '2': 'validate_task.html',
               '3': 'submit_task.html',
               '4': 'approve_task.html'}

    save_functions={'1': 'create',
                    '2': 'validate',
                    '3': 'submit',
                    '4': 'approve'}

    actors={'1': 'creator',
            '2': 'validator',
            '3': 'implementer',
            '4': 'approver'}

    form=forms[page]
    template=templates[page]
    save_function=save_functions[page]
    actor=actors[page]

    fields=form.base_fields

    # get task instance
    task = get_object_or_404(Task, pk=pk)

    # get task state
    state=task.state

    # get instance of the user whom the request is coming from
    user = request.user

    # get instance of corresponding employee
    employee = Employee.objects.filter(user__pk=user.pk)[0]

    # get authorized actor
    authorized_actor=getattr(task,actor)

    # determine writing rights of employee
    is_write=write_permission(page, state, employee, authorized_actor)

    if request.method == "POST":

        # if user strikes cancel, redirect to task list
        if request.POST.get("cancel"):
            return redirect('task:list')

        # handles form submitted by user
        form = form(request.POST)

        #if not is_write:
        #    disable_form(form)
        print("form is valid: %r" % form.is_valid())

        if form.is_valid():

            # get data provided by user
            cleaned_data = form.cleaned_data

            # create new taskviews.py
            for field in fields:
                setattr(task, field, cleaned_data[field])

            # add automatic fields and save instance to db, with the help of model saving methods (1 method by wizard page)
            save_function=getattr(task,save_function)
            save_function(employee)

            # if everything goes well, redirect to task list
            return redirect("task:list")

    else:

        # create context
        context={field: getattr(task,field) for field in fields}

        # delivers a blank form to be filled in
        form = form(context)

        #if not is_write:
        #    print("disable form")
        #    disable_form(form)

    # render form using given html template
    return render(request, template, {'form': form, 'page': page, 'pk': pk, 'wizard_titles':wizard_titles, 'state':state})



def write_permission(page_string, state_string, employee, authorized_actor):

    is_write=False
    print("employee type: %s" % type(employee.pk))
    print("authorized_actor type: %s" % type(authorized_actor.pk))
    print("state type: %s" % type(state_string))
    print(state_string)
    print("page type: %s" % type(page_string))
    state=int(state_string)
    page=int(page_string)
    if employee.pk == authorized_actor.pk:
        if state>=page -1 and state<=page:
            is_write=True


    print("page: %s" % page)
    print("state: %s" % state)
    print("employee: %s" % employee)
    print("authorized_actor: %s" % authorized_actor)



    if is_write:
        print("%s has %s permission" % (employee, page))
    else:
        print("%s has NO %s permission" % (employee, page))

    return is_write



def disable_form(form):
    for field in form.fields:
        #form.fields[field].required=False
        form.fields[field].widget.attrs['disabled'] = 'disabled'


@login_required
def delete(request,pk):

    task = get_object_or_404(Task, pk=pk)

    task.delete()

    return redirect("task:list")


