from django import forms


class CreateOrderForm(forms.Form):
    first_name = forms.CharField(label='Имя', max_length=100, required=True)
    last_name = forms.CharField(label='Фамилия', max_length=100, required=True)
    phone_number = forms.CharField(label='Номер телефона', max_length=12, required=True)
    delivery_method = forms.ChoiceField(label='Способ доставки', choices=[(0, 'Самовывоз'), (1, 'Доставка')])
    address = forms.CharField(label='Адрес доставки', max_length=255, required=False)
    payment_method = forms.ChoiceField(label='Способ оплаты', choices=[(0, 'Оплата наличными'), (1, 'Оплата картой')])

    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Введите ваше имя",
    #         })
    # )
    #
    # last_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Введите вашу фамилию",
    #         }
    #     )
    # )
    #
    # phone_number = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Введите номер телефона",
    #         }
    #     )
    # )
    #
    # requires_delivery = forms.ChoiceField(
    #     widget=forms.RadioSelect(),
    #     choices=[
    #         ("0", False),
    #         ("1", True),
    #     ],
    #     initial=0,
    # )
    #
    # delivery_address = forms.CharField(
    #     widget=forms.Textarea(
    #         attrs={
    #             "class": "form-control",
    #             "id": "delivery-address",
    #             "row": 2,
    #             "placeholder": "Введите адрес доставки"
    #         }
    #     ),
    #     required=False,
    # )
    #
    # payment_on_get = forms.ChoiceField(
    #     widget=forms.RadioSelect(),
    #     choices=[
    #         ("0", 'False'),
    #         ("1", 'True'),
    #
    #     ],
    #     initial="card",
    # )
