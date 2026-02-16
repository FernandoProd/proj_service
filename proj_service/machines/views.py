from django.shortcuts import render, redirect
from .models import Machine
from .forms import MachineForm
from django.views.generic import DetailView, UpdateView, DeleteView


def machines_home(request):
    machines = Machine.objects.all()
    return render(request, 'machines/machines_home.html', {'machines':machines})


class MachineDetailView(DetailView):
    model = Machine
    template_name = 'machines/machine_detail.html'
    context_object_name = 'machine'


class MachineUpdateView(UpdateView):
    model = Machine
    template_name = 'machines/create.html'

    form_class = MachineForm


class MachineDeleteView(DeleteView):
    model = Machine
    success_url = '/machines/'
    template_name = 'machines/machines-delete.html'


def create(request):
    if request.method == 'POST':                           #Если мы нажмем кнопу добавить, то выполнится данная проверка
        form = MachineForm(request.POST)                   #Здесь мы получаем все данные, которые ввел пользователь
        if form.is_valid():                                #Проверяет корректно ли заполнены данные
            form.save()                                    #Сохраняем новую запись в базу данных
            return redirect('machines_home')               #Если сохранились данные, то автоматически переадресуется клиент на гл. страницу

    form = MachineForm()

    data = {
        'form': form
    }
    return render(request, 'machines/create.html', data)
