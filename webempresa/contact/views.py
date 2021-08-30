from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm


def contact(request: WSGIRequest):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Envio de email
            email = EmailMessage(
                subject='Mensaje de pruebas Django',
                body=f"De {name} Escribio {content}",
                from_email='test@mailtrap.com',
                to=['tavo9601@gmail.com']
            )
            try:
                email.send()
                return redirect(reverse('contact') + '?ok')
            except:
                return redirect(reverse('contact') + '?fail')


    return render(request=request, template_name='contact/contact.html', context={'contact_form': contact_form})
