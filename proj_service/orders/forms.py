from django import forms
from .models import Order, OrderDetail

# Форма для заявки
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_number', 'priority', 'customer_name', 'status']

# Форма для деталей заявки
class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = ['detail', 'quantity']

# Форма набора форм для деталей заявки (formset)
from django.forms import inlineformset_factory
#
#OrderDetailFormSet = inlineformset_factory(
#    Order,  # Модель, с которой будет связан formset
#    OrderDetail,  # Модель, которую нужно будет редактировать через formset
#    form=OrderDetailForm,  # Используемая форма для деталей
#    extra=3,  # Количество пустых форм по умолчанию
#    can_delete=True  # Возможность удалять детали
#)

from django import forms
from django.forms import modelformset_factory
from .models import OrderDetail

class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = ['detail', 'quantity']

# Formset для нескольких деталей
OrderDetailFormSet = modelformset_factory(
    OrderDetail, form=OrderDetailForm, extra=1  # 'extra=1' добавляет одну пустую форму
)