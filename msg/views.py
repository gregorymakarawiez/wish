from django.shortcuts import render, get_object_or_404, redirect
from .models import Message
from .forms import EditForm



def list(request):

    template='list_messages.html'

    messages = Message.objects.all()
    return render(request,template, {'messages': messages} )




def create(request):

    Form=EditForm
    template='create_message.html'

    if request.method == "POST":

        # handles form submitted by user
        form = Form(request.POST)

        if form.is_valid():

            # get data provided by user
            cleaned_data = form.cleaned_data

            # create new task
            message = Message()
            message.create(cleaned_data["message"])

            # if everything goes well, redirect to task list
            return redirect("msg:list")

    else:
        # delivers a blank form to be filled in
        form = Form()

    # render form using given html template
    return render(request, template, {'form': form})





def edit(request,pk):

    # get task instance
    message = get_object_or_404(Message, pk=pk)

    Form=EditForm
    fields=Form.base_fields
    template='edit_message.html'

    if request.method == "POST":

        # if user strikes cancel, redirect to task list
        if request.POST.get("cancel"):
            return redirect('msg:list')

        # handles form submitted by user
        form = EditForm(request.POST)

        if form.is_valid():

            # get data provided by user
            cleaned_data = form.cleaned_data

            # create new task
            for field in fields:
                setattr(message, field, cleaned_data[field])

            # add automatic fields and save instance to db, with the help of model saving methods (1 method by wizard page)
            message.save()

            # if everything goes well, redirect to task list
            return redirect("msg:list")

    else:

        # create context
        context={field: getattr(message,field) for field in fields}

        # delivers a blank form to be filled in
        form = Form(context)


    # render form using given html template
    return render(request, template, {'form': form, 'pk': message.pk})


def test(request):

    template='test_quill.html'

    return render(request, template)



def test2(request):

    Form=EditForm
    template='test_quill2.html'

    if request.method == "POST":

        # if user strikes cancel, redirect to task list
        if request.POST.get("cancel"):
            return redirect('msg:list')

        # handles form submitted by user
        form = Form(request.POST)

        if form.is_valid():

            # get data provided by user
            cleaned_data = form.cleaned_data

            # create new task
            message = Message()
            message.create(cleaned_data["message"])

            # if everything goes well, redirect to task list
            return redirect("msg:list")

    else:
        # delivers a blank form to be filled in
        form = Form()

    # render form using given html template
    return render(request, template, {'form': form})