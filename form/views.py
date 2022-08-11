from django.shortcuts import render
from django.http import HttpResponseRedirect
from form.forms import INPUT_CLASSES, SignupForm
from form.service import signup_user


def send_form(request):
    if request.method == 'GET':
        form = SignupForm()
    elif request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            signup_user(
                email=form.cleaned_data['email'],
                full_name=form.cleaned_data['full_name'],
            )
            return HttpResponseRedirect('/thanks/')

    return render(request, 'form.html', {
        'form': form,
        'input_classes': INPUT_CLASSES
    })

