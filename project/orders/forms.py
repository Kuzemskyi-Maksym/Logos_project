from django import forms

class CreateOrderForm(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    requires_delivery = forms.ChoiceField()
    

    requires_delivery = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=[
            {"0", False},
            {"1", True},
        ],
        initial=0,
    )


    payment_on_get = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=[
            {"0", False},
            {"1", True},
        ],
        initial=0,
    )




    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             # "required": "",
    #             # "name": "password",
    #             # "id": "password",
    #             # "type": "password",
    #             "class": "w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5",
    #             "placeholder": "First Name",
    #             "style": "height: 50px !important; margin-top: 20px !important;",
    #             # "maxlength": "22",
    #             # "minlength": "8",
    #         }
    #     )
    # )

    # last_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             # "required": "",
    #             # "name": "last_name",
    #             # "id": "last_name",
    #             # "type": "text",
    #             "class": "form-input w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5",
    #             "placeholder": "Last Name",
    #             "style": "height: 50px !important; margin-top: 20px !important;",
    #         }
    #     )
    # )

    # phone_number = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             # "required": "",
    #             # "name": "password",
    #             # "id": "password",
    #             # "type": "password",
    #             "class": "w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5",
    #             "placeholder": "Phone Number",
    #             "style": "height: 50px !important; margin-top: 20px !important;",
    #             # "maxlength": "22",
    #             # "minlength": "8",
    #         }
    #     )
    # )

    

    # delivery_address = forms.CharField(
    #     widget=forms.Textarea(
    #         attrs={
    #             # "required": "",
    #             # "name": "password",
    #             "id": "delivery-address",
    #             # "type": "password",
    #             "rows": 2,
    #             "class": "w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5",
    #             "placeholder": "Adress",
    #             "style": "height: 50px !important; margin-top: 20px !important;",
    #             # "maxlength": "22",
    #             # "minlength": "8",
    #         }
    #     )
    #     required=False
    # )

    
