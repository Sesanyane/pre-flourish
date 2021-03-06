from django import template
from django.conf import settings


register = template.Library()


@register.inclusion_tag('pre_flourish/buttons/consent_button.html')
def consent_button(model_wrapper):
    title = ['Consent subject to participate.']
    return dict(
        subject_identifier=model_wrapper.consent.object.subject_identifier,
        subject_screening_obj=model_wrapper.object,
        add_consent_href=model_wrapper.consent.href,
        # consent_version=model_wrapper.consent_version,
        title=' '.join(title))


@register.inclusion_tag('pre_flourish/buttons/dashboard_button.html')
def dashboard_button(model_wrapper):
    pre_flourish_subject_dashboard_url = settings.DASHBOARD_URL_NAMES.get(
        'pre_flourish_subject_dashboard_url')
    return dict(
        pre_flourish_subject_dashboard_url=pre_flourish_subject_dashboard_url,
        subject_identifier=model_wrapper.subject_identifier)


@register.inclusion_tag('flourish_dashboard/buttons/locator_button.html')
def locator_button(model_wrapper):
    return dict(
        add_locator_href=model_wrapper.caregiver_locator.href,
        screening_identifier=model_wrapper.object.screening_identifier,
        caregiver_locator_obj=model_wrapper.locator_model_obj)


@register.inclusion_tag('pre_flourish/buttons/edit_screening_button.html')
def edit_screening_button(model_wrapper):
    title = ['Edit Subject Screening form.']
    return dict(
        screening_identifier=model_wrapper.object.screening_identifier,
        href=model_wrapper.href,
        title=' '.join(title))
