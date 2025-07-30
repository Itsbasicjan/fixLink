# fixlinkv2/signals.py
from django.db.models.signals import pre_save
from django.dispatch import receiver
from part.models import Part

@receiver(pre_save, sender=Part)
def replace_empty_link(sender, instance, **kwargs):
    """
    Wenn der externe Link als leerer String kommt,
    ersetze ihn kurz vor dem Speichern durch None.
    Dadurch akzeptiert das URLField den Wert und
    landet als NULL in der DB.
    """
    if instance.link == "":
        instance.link = None
