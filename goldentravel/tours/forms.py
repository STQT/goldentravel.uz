from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button
from django import forms
from django.urls import reverse_lazy, reverse
from django.utils.translation import gettext_lazy as _


class TourForm(forms.Form):
    def __init__(self, obj, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['tour'] = forms.fields.Field(disabled=True, initial=)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('tours:detail', kwargs={'pk': obj.pk})
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', "Submit"))
        self.helper.add_input(Button('cancel', _('Публичная офферта'), css_class='btn-gray',
                                     onclick="window.location.href = '{}';".format(reverse('public_offer'))))

    fullname = forms.CharField(max_length=100)
    email = forms.EmailField()
    offer_check = forms.BooleanField(error_messages={'required': _('Пожалуйста, прочтите и примите'
                                                                   'публичную офферту'), })

    class Meta:
        labels = {"offer_check": "Qale ishlar" }
