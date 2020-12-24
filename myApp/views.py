import datetime
from django.shortcuts import render, redirect
from .models import ToDo
from .forms import AddForm

# Create your views here.
def home(request):
    to_dos = ToDo.objects.all()

    today = datetime.date.today()
    expired = to_dos.filter(due_date__lt=today).order_by('due_date')
    prompt = to_dos.filter(due_date__gte=today).\
        filter(due_date__lte=today+datetime.timedelta(days=7)).order_by('due_date')
    normal = to_dos.filter(due_date__gt=today+datetime.timedelta(days=7)).order_by('due_date')

    context = {
        'expired': expired,
        'prompt': prompt,
        'normal': normal,
    }
    return render(request, 'myApp/home.html', context)

def add(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddForm()
    return render(request, 'myApp/add.html', {'form': form})

def delete(request, pk):
    target = ToDo.objects.get(id=pk)
    target.delete()
    return redirect('home')
