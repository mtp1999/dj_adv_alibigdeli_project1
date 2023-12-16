from django.test import TestCase
from appBlog import forms
from captcha.models import CaptchaStore


class TestForm(TestCase):
    def test_contact_form_valid_data(self):
        CaptchaStore.generate_key()
        captcha = CaptchaStore.objects.all()[0]
        form = forms.ContactForm(
            data={
                "name": "Jax",
                "email": "jax.jax@gmail.com",
                "subject": "comment subj",
                "message": "comment message",
                "captcha_0": captcha.hashkey,
                "captcha_1": captcha.response,
            }
        )
        # print(form.is_valid(), form.errors)
        self.assertTrue(form.is_valid())
