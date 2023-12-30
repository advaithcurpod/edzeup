from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    ROLE_CHOICES = [
        ('Lead', 'Lead'),
        ('Subordinate', 'Subordinate'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Subordinate')

    def __str__(self):
        return self.username

@receiver(post_save, sender=User)
def add_user_to_group(sender, instance, **kwargs):
    print('Signal Triggered')
    if instance.role == 'Lead':
        print('Lead')
        lead_group = Lead.objects.get_or_create(name='Lead')[0]
        instance.groups.add(lead_group)
        lead_group.save()

    elif instance.role == 'Subordinate':
        print('Subordinate')
        subordinate_group = Subordinate.objects.get_or_create(name='Subordinate')[0]
        instance.groups.add(subordinate_group)
        subordinate_group.save()

# Connect the signal
post_save.connect(add_user_to_group, sender=User)

class Lead(Group):
    class Meta:
        proxy = True

class Subordinate(Group):
    class Meta:
        proxy = True
