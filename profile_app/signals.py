from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from profile_app import model_choices as mch
from profile_app.models import Customer, Logger
from django.conf import settings


@receiver(post_save, sender=Customer)
def post_save_customer(sender, instance, created, **kwargs):

    customer_id = instance.id
    if created:
        action = mch.ACT_CREATE
    else:
        action = mch.ACT_EDIT

    rate_kwargs = {
        'user': customer_id,
        'action': action,
    }
    rate = Logger(**rate_kwargs)
    rate.save()


@receiver(pre_delete, sender=Customer)
def pre_delete_customer(sender, instance, created, **kwargs):

    customer_id = instance.id
    rate_kwargs = {
        'user': customer_id,
        'action': mch.ACT_DELETE,
    }
    rate = Logger(**rate_kwargs)
    rate.save()
