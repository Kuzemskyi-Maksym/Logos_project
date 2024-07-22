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
