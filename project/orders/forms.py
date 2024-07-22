import re
from django import forms

class CreateOrderForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    delivery_address = forms.CharField(widget=forms.Textarea, required=False)
    requires_delivery = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=[
            ('0', 'Self-delivery'),
            ('1', 'Need delivery'),
        ],
        initial='0',
    )
    payment_on_get = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=[
            ('0', 'Payment by card'),
            ('1', 'Cash/card on receipt'),
        ],
        initial='0',
    )

    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']

        if not data.isdigit():
            raise forms.ValidationError('The phone number can only contain digits')
        
        pattern = re.compile(r'^\d{10}$')
        if not pattern.match(data):
            raise forms.ValidationError('The phone number must be 10 digits long')
        
        return data

