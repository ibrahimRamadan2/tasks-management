from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_confirmation_mail(user_email , token): 
    template_name = "account/email/email_confirmation_message.html"
    convert_to_html_content =  render_to_string(template_name=template_name , context={'token':token})
    plain_message = strip_tags(convert_to_html_content)
    
    
    send_mail( subject="Email confirmation",
        message=plain_message,
        from_email="iramadan@lucidya.com",
        recipient_list=[user_email],
        fail_silently=False,
        html_message=convert_to_html_content
    )
    


