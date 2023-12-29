from django.shortcuts import render
from django.contrib import messages
from django.core.mail import EmailMessage
from .forms import ApplicationForm
from .models import Form



def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            Form.objects.create(first_name=first_name, last_name=last_name,
                                email=email, date=date, occupation=occupation)
            
            message_body = f"Thank you for your submission.\n"\
                       f"Here is your submitted data:\n{first_name} {last_name}\n{date}\n{occupation}\n\n"\
                       f"Thank you.\n"\
                       f"Innovative Technology"
            email_message = EmailMessage("New Job Application", message_body, to=[email])
            email_message.send()

            messages.success(request, "Form Submitted Successfully")

    return render(request, "index.html")


def about(request):
    return render(request, "about.html")
