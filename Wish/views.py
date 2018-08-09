
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from account.models import Employee


@login_required
def base(request):
    return render(request, 'base_.html')



@login_required
def home(request):

    # get instance logged logged employee
    user=request.user
    employee=Employee.objects.filter(user__pk=user.pk)

    return render(request,"base_site.html",{'employee':employee})


def debug(request):

    # get instance logged logged employee
    return render(request,"debug.html")