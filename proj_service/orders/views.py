from django.shortcuts import render, redirect
from .models import Order, OrderDetail
from .forms import OrderForm, OrderDetailFormSet

def orders_home(request):
    orders = Order.objects.all()
    return render(request, 'orders/orders_home.html', {
        'orders': orders
    })

def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    order_details = OrderDetail.objects.filter(order=order)
    return render(request, 'orders/order_detail.html', {
        'order': order,
        'order_details': order_details
    })


def create_order(request):
    if request.method == 'POST':
        formset = OrderDetailFormSet(request.POST)
        if formset.is_valid():
            #Создается заказ
            order_number = request.POST.get('order_number')
            order = Order.objects.create(order_number=order_number)

            #Сохраняем детали
            for form in formset:
                if form.cleaned_data:
                    detail = form.cleaned_data['detail']
                    quantity = form.cleaned_data['quantity']
                    OrderDetail.objects.create(order=order, detail=detail, quantity=quantity)

            return redirect('orders_home')
    else:
        formset = OrderDetailFormSet(queryset=OrderDetail.objects.none())

    return render(request, 'orders/create_order.html', {'formset': formset})