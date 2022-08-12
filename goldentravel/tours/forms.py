from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Field
from django import forms
from django.urls import reverse_lazy


class TourForm(forms.Form):
    def __init__(self, obj, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['tour'] = forms.fields.Field(disabled=True, initial=)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('tours:detail', args=(obj.id,))
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', "Submit"))

    fullname = forms.CharField(max_length=100)
    email = forms.EmailField()
