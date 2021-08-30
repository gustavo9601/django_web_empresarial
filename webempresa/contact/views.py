from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm


def contact(request: WSGIRequest):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Si todo ok
            return redirect(reverse('contact')+'?ok')


    return render(request=request, template_name='contact/contact.html', context={'contact_form': contact_form})
