from django import forms
from .models import Item, Issue, Receive

class AddItemForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ('created_by', 'date_created', 'recent_quantity')

class IssueItemForm(forms.ModelForm):
    class Meta:
        model =  Issue
        exclude = ('issued_by', 'issued_on', 'quantity_remaining')

class ReceiveItemForm(forms.ModelForm):
    class Meta:
        model = Receive
        exclude = ('received_by', 'quantity_remaining', 'received_on')

class UpdateRestockForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['restock_amount']
        

    