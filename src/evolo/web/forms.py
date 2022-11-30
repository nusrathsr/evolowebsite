from django import forms
from django.forms import ModelForm
from django.forms.widgets import EmailInput, TextInput
from web.models import Contact, INTERESTED_IN


EMPTY_INTERESTED_IN = (("", "Interested In..."),) + INTERESTED_IN


class ContactForm(ModelForm):
    interested_in = forms.ChoiceField(choices=EMPTY_INTERESTED_IN)

    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            "full_name": TextInput(attrs={"placeholder": "Full Name"}),
            "email": EmailInput(attrs={"placeholder": "Email"}),
            "phone": TextInput(attrs={"placeholder": "Phone"}),
        }
