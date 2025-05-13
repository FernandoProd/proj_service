from .models import Order, OrderDetail
from django import forms
from django.forms import modelformset_factory
from .models import OrderDetail


      #Форма для заявки
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_number', 'priority', 'customer_name', 'status']

   #Форма для деталей заявке
class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = ['detail', 'quantity']


class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = ['detail', 'quantity']

#Чтобы доваить несколько деталей в заявку
OrderDetailFormSet = modelformset_factory(
    OrderDetail, form=OrderDetailForm, extra=1
)