from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Item, Receive, Issue
from .form import AddItemForm, IssueItemForm, ReceiveItemForm, UpdateRestockForm


@login_required
def DashboardView(request):
    obj = Item.objects.filter(recent_quantity = 0)[:1]
    context = {'obj':obj}
    return render(request, 'store/dashboard.html', context)

@login_required
def AllItemsView(request):
    obj = Item.objects.all()
    context = {'obj':obj}
    return render(request, 'store/all_items.html', context)

@login_required
def IssueHistoryView(request):
    obj = Issue.objects.all()
    context = {'obj':obj}
    return render(request, 'store/issue_history.html', context)

@login_required
def ReceiveHistoryView(request):
    obj = Receive.objects.all()
    context = {'obj':obj} 
    return render(request, 'store/receive_history.html', context)

@login_required
def AddItemView(request):
    obj = Item.objects.all().order_by('-date_created')[:5]
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.created_by = request.user
            var.recent_quantity = var.quantity
            var.save()
            return redirect('add-item')
    else:
        form =  AddItemForm()
    context = {'form':form, 'obj':obj}
    return render(request, 'store/add_item.html', context)

@login_required
def IssueItemView(request):
    obj1 = Issue.objects.all().order_by('-issued_on')[:5]
    if request.method == 'POST':
        form = IssueItemForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            obj = Item.objects.get(name=str(var.item))
            obj.recent_quantity = obj.recent_quantity - var.quantity_issued
            var.quantity_remaining = obj.recent_quantity
            var.issued_by = request.user
            obj.save()
            var.save()
            return redirect('issue-item')
    else:
        form = IssueItemForm
    context = {'form':form, 'obj1':obj1}
    return render(request, 'store/issue_item.html', context)

@login_required
def ReceiveItemView(request):
    obj1 = Receive.objects.all().order_by('-received_on')[:5]
    if request.method == 'POST':
        form = ReceiveItemForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            obj = Item.objects.get(name=str(var.item))
            obj.recent_quantity = obj.recent_quantity + var.quantity_received
            var.quantity_remaining = obj.recent_quantity
            var.received_by = request.user
            obj.save()
            var.save()
            return redirect('receive-item')
    else:
        form = ReceiveItemForm
    context = {'form':form, 'obj1':obj1}
    return render(request, 'store/receive_item.html', context)

@login_required
def UpdateRestockView(request, pk):
    obj = Item.objects.get(id=pk)
    if request.method == 'POST':
        form = UpdateRestockForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UpdateRestockForm(instance=obj)
    context = {'form':form}
    return render(request, 'store/update_restock.html', context)

@login_required
def FinishedItemsView(request):
    obj = Item.objects.filter(recent_quantity = 0)
    context = {'obj':obj}
    return render(request, 'store/finished_items.html', context)