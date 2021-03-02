from django.template import Context
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMessage

def send_contact_email(full_name, email, phone_number, message):
    context = {
        'full_name': full_name,
        'email': email,
        'phone_number': phone_number,
        'message': message,
    }

    email_subject = 'Contact Message | Portfolio'

    email_body = render_to_string('email_message.txt', context)


    email = EmailMessage(
        email_subject, email_body,
        settings.DEFAULT_FROM_EMAIL, ['youremail@email.com', ],
    )

    return email.send(fail_silently=False)