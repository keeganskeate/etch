import os
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.conf import settings
# from django.core.mail import send_mail

from .forms import ContactForm
from . import state # Save text in Firestore?
from utils.utils import load_markdown

def create_page_context(context, markdown_file=None, options=None):
    """ Create context for a normal page. """
    context["state"] = state.state
    context["header"] = state.header
    context["footer"] = state.footer
    if markdown_file:
        file_path = os.path.dirname(os.path.realpath(__file__))
        context = load_markdown(context, file_path, markdown_file, options)
    return context

class HomePageView(TemplateView):
    """ Home page. """

    template_name = settings.PROJECT_NAME + "/homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = create_page_context(context)
        context['homepage'] = state.homepage
        return context


class AboutView(TemplateView):
    """ About page. """

    template_name = settings.PROJECT_NAME + "/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = create_page_context(context, markdown_file="about")
        return context


class ContactView(FormView):
    """ Contact page. """

    form_class = ContactForm
    template_name = settings.PROJECT_NAME + "/contact.html"
    success_url = '/thank-you/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = create_page_context(context)
        return context

    def form_valid(self, form):
        form.send_email()
        return super(ContactView, self).form_valid(form) 


class PrivacyPolicyView(TemplateView):
    """ Privacy Policy page. """

    template_name = settings.PROJECT_NAME + "/privacy-policy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = create_page_context(context, markdown_file="privacy_policy")
        return context


class TermsOfServiceView(TemplateView):
    """ Terms of Service page. """

    template_name = settings.PROJECT_NAME + "/terms-of-service.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = create_page_context(context, markdown_file="terms_of_service")
        return context


class ThankYouView(TemplateView):
    """ Thank you page. """

    template_name = settings.PROJECT_NAME + "/thank-you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = create_page_context(context)
        return context
