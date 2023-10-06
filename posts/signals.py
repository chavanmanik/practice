# # posts/signals.py
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.core.mail import send_mail
# from .models import Post

# @receiver(post_save, sender=Post)
# def send_post_creation_notification(sender, instance, **kwargs):
#     subject = 'New Post Created'
#     message = f'Your post "{instance.title}" has been created successfully.'
#     from_email = 'chavanmanik.cm@gmail.com'  # Update with your email
#     recipient_list = [instance.author.email]
#     send_mail(subject, message, from_email, recipient_list)

# posts/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Post

@receiver(post_save, sender=Post)
def send_post_creation_notification(sender, instance,created, **kwargs):
    if created:
        subject = 'New Post Created'
        message = f'Your post "{instance.title}" has been created successfully.'
        from_email = 'manikchavan557@gmail.com'  # Use the email specified in settings.py
        recipient_list = [instance.author.email]
        send_mail(subject, message, from_email, recipient_list)
