# -*- coding: utf-8 -*-
from django import forms
from django.utils import timezone


class OrderForm(forms.Form):
    name = forms.CharField()
    last_name = forms.CharField(required=False)
    phone = forms.CharField()
    buying_type = forms.ChoiceField(widget=forms.Select(), choices=([("self", "Самовывоз"),("delivery", "Доставка")]))
    date = forms.DateField(widget=forms.SelectDateWidget(), initial=timezone.now())
    address=forms.CharField(required=False)
    comments= forms.CharField(widget=forms.Textarea, required=False)


    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['name'].lable = 'Имя'
        self.fields['last_name'].lable = 'Фамилия'
        self.fields['phone'].lable = 'Контактный телефон'
        self.fields['phone'].help_text = 'Пожалуйста, указывайте реальный номер, по которому с Вами можно связаться'
        self.fields['buying_type'].lable = 'Спрособ получения'
        self.fields['address'].lable = 'Адрес доставки'
        self.fields['address'].help_text = '*Обязательно указывайте город!'
        self.fields['comments'].lable = 'Комментарий к заказу'
        self.fields['date'].lable = 'Дата доставки'
        self.fields['date'].help_text = 'Доставка произвадится на следующий день после даты заказа'



