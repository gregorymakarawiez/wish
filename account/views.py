from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def signin(request):

    from .forms import SigninForm
    from django.contrib.auth import authenticate, login

    if request.method == "POST":

        # handles form submitted by user
        form = SigninForm(request.POST)


        if form.is_valid():

            # get data provided by user
            cleaned_data = form.cleaned_data

            # get credentials
            username=cleaned_data['username']
            password=cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                # redirect employee to home
                return redirect("task:list")

    else:
        # delivers a blank form to be filled in
        form = SigninForm()

    # render form using given html template
    return render(request, 'signin.html', {'form': form})


def signup(request):

    from django.contrib.auth.models import User
    from .models import Employee
    from .forms import SignupForm


    employee_fields=['unit',
                     'manager',
                     'is_manager',
                     'is_continuous_improvement_officer',
                     'subscribed_to_newsletter']

    if request.method == "POST":

        # if user strikes cancel, redirect to sigin view
        if request.POST.get("cancel"):
            return redirect('account:signin')


        # handles form submitted by user
        form = SignupForm(request.POST)


        if form.is_valid():

            # get data provided by user
            cleaned_data = form.cleaned_data

            # create new user
            user=User.objects.create_user(
                first_name=cleaned_data['first_name'],
                last_name = cleaned_data['last_name'],
                username = cleaned_data['username'],
                password = cleaned_data['password'],
                email = cleaned_data['email']
            )

            # save user in database
            user.save()

            # create new employee
            employee = Employee(user=user)
            for field in employee_fields:
                setattr(employee, field, cleaned_data[field])

            # save employee
            employee.save()

            # if everything goes well, redirect employee to signin page
            return redirect("account:signin")

    else:
        # delivers a blank form to be filled in
        form = SignupForm()


    # render form using given html template
    return render(request, 'signup.html', {'form': form})



@login_required
def profile(request):

    from django.contrib.auth.models import User
    from .models import Employee
    from .forms import ProfileForm


    user_fields=     ['first_name',
                     'last_name',
                     'username',
                     'password',
                     'email']
    employee_fields=['unit',
                     'manager',
                     'is_manager',
                     'is_continuous_improvement_officer',
                     'subscribed_to_newsletter']

    # get instance of the user that is editing his/her profile
    user = request.user

    # get instance of the employee that is editing his/her profile
    employee = Employee.objects.filter(user__pk=user.pk)[0]


    if request.method == "POST":

        # if user strikes cancel, redirect to task list
        if request.POST.get("cancel"):
            return redirect('task:list')

        # handles form submitted by user
        form = ProfileForm(request.POST)

        # validate form
        form.clean()

        if form.is_valid():

            # get data provided by user
            cleaned_data = form.cleaned_data



            # update userfields
            for field in user_fields:
                setattr(user, field, cleaned_data[field])

            # save user changes in database
            user.save()

            # update userfields
            for field in employee_fields:
                setattr(employee, field, cleaned_data[field])

            # save employee changes in database
                employee.save()

            # if everything goes well, redirect employee to task list
            return redirect('task:list')

    else:

        context={'first_name':employee.user.first_name,
                 'last_name':employee.user.last_name,
                 'username':employee.user.username,
                 'password':employee.user.password,
                 'email':employee.user.email,
                 'unit':employee.unit,
                 'manager':employee.manager,
                 'is_manager':employee.is_manager,
                 'is_continuous_improvement_officer':employee.is_continuous_improvement_officer,
                 'subscribed_to_newsletter':employee.subscribed_to_newsletter,
                }
        # delivers a blank form to be filled in
        form = ProfileForm(context)


    # render form using given html template
    return render(request, 'profile.html', {'form': form})