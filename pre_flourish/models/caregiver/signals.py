from django.apps import apps as django_apps
from django.db.models.signals import post_save
from django.dispatch import receiver

from edc_visit_schedule.site_visit_schedules import site_visit_schedules

from .caregiver_child_screening_consent import CaregiverChildScreeningConsent


@receiver(post_save, weak=False, sender=CaregiverChildScreeningConsent,
          dispatch_uid='caregiver_child_consent_on_post_save')
def caregiver_child_consent_on_post_save(sender, instance, raw, created, **kwargs):
    """Creates an onschedule instance for this enrolled subject, if
    it does not exist.
    """
    if not raw:
        if not created:
            _, schedule = site_visit_schedules.get_by_onschedule_model(
                'pre_flourish.onschedulepreflourish')
            schedule.refresh_schedule(
                subject_identifier=instance.subject_identifier)
        else:
            # put subject on schedule
            _, schedule = site_visit_schedules.get_by_onschedule_model(
                'pre_flourish.onschedulepreflourish')
            schedule.put_on_schedule(
                subject_identifier=instance.subject_identifier,
                onschedule_datetime=instance.consent_datetime)
