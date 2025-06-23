from django.core.mail import EmailMessage
from django.conf import settings
from celery import shared_task

def send_email(subject, body, to_addresses, attachments=None):    
    try:
        # Create the email message
        email = EmailMessage(
            subject = subject,                # Email subject
            body = body,                   # Email body
            from_email = settings.DEFAULT_FROM_EMAIL,  # From email (defined in settings)
            to=to_addresses,           # List of recipient email addresses
        )


        # Add attachments if provided
        if attachments:
            print("attachments", attachments)
            for attachment, file_name in attachments:
                # Attach file directly from the file-like object
                email.attach(file_name, attachment.read(), attachment.content_type)
        
        # Send the email
        email.send(fail_silently=False)
        print("Email sent successfully.")
    
    except Exception as e:
        print(f"Error sending email: {e}")


@shared_task
def send_email_helper(receipants):
    send_email("Registration Successful", "Welcome to Khanha Lal", receipants)