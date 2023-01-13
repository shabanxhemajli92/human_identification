from django.shortcuts import render, redirect
from .forms import HumanForm
from .models import Human

def create_human(request):
    if request.method == 'POST':
        form = HumanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_humans')
    else:
        form = HumanForm()
    return render(request, 'identification/create_human.html', {'form': form})

def view_humans(request):
    filter_name = request.GET.get('name')
    if filter_name and filter_name != "Select a name":
        human = Human.objects.filter(full_name__exact=filter_name).first()
        context = {'human': human}
        return render(request, 'identification/view_humans.html', context)
    else:
        humans = Human.objects.all()
        context = {'humans': humans}
        return render(request, 'identification/view_humans.html', context)    
