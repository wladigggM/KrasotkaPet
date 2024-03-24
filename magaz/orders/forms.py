from django import forms


class CreateOrderForm(forms.Form):
    first_name = forms.CharField(label='Имя', max_length=100, required=True)
    last_name = forms.CharField(label='Фамилия', max_length=100, required=True)
    phone_number = forms.CharField(label='Номер телефона', max_length=12, required=True)
    delivery_method = forms.ChoiceField(label='Способ доставки', choices=[(0, 'Самовывоз'), (1, 'Доставка')])
    address = forms.CharField(label='Адрес доставки', max_length=255, required=False)
    payment_method = forms.ChoiceField(label='Способ оплаты', choices=[(0, 'Оплата наличными'), (1, 'Оплата картой')])

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']

        if not phone_number.isdigit():
            raise forms.ValidationError('Номер телефона должен содержать только цифры')

        return phone_number
