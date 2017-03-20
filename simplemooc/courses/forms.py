from django import forms
from django.conf import settings
from simplemooc.core.mail import send_email_template


class ContactCourse(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Mensagem/Dúvida', widget=forms.Textarea)

    def send_email(self, course):
        subject = '{} Contato'.format(course)
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message']
        }
        send_email_template(
            subject,
            'courses/contact_email.html',
            context,
            [settings.CONTACT_EMAIL]
        )
