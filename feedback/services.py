import mandrill

from django.conf import settings
from django.template import loader

def send_feedback_creation_email(request, questionnaire):
    mandrill_client = mandrill.Mandrill(settings.MANDRILL_API_KEY)
    mandrill_client.messages.send({
        'from_email': 'info@peopleskillsforgeeks.com',
        'from_name': 'People Skills For Geeks',
        'subject': 'Feedback Form',
        'html': loader.render_to_string('emails/admin_link.html', {
            'asker_name': questionnaire.asker_name,
            'form_url': request.build_absolute_uri(questionnaire.get_url()),
            'form_admin_url': request.build_absolute_uri(questionnaire.get_admin_url()),
        }),
        'auto_text': True,
        'to': [{
            'email': questionnaire.asker_email,
            'name': questionnaire.asker_name,
        }],
        'track_clicks': False,
        'track_opens': False,
    })
