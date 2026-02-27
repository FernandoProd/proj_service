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
    if request.method == 'POST':
        form = MachineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('machines_home')

    form = MachineForm()

    data = {
        'form': form
    }
    return render(request, 'machines/create.html', data)
