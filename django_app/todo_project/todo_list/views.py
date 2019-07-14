from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method == 'POST':
        item = request.POST['item']
        
        form = List(item=item)
        form.save()
        all_items = List.objects.all()
        messages.success(request, ('Item has been added to the list'))
        return render(request, 'home.html', {'all_items': all_items})
    else:
        all_items = List.objects.all()
        return render(request, 'home.html', {'all_items': all_items})
    
def deleteView(request, list_id):
    result = List.objects.filter(pk=list_id)
    result.delete()
    messages.warning(request, ('Record deleted from the list!'))
    return redirect('home')
    
def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')

def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')

def edit(request, list_id):
    if request.method == 'POST':
        inp_value = request.POST['item']
        result = List.objects.filter(pk=list_id).update(item=inp_value)
        
        messages.success(request, ('Item has been edited!'))
        return redirect('home')
    
    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})