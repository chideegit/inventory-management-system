from store.form import UpdateRestockForm
from django.urls import path 
from .views import DashboardView, AllItemsView, ReceiveHistoryView, IssueHistoryView, \
    AddItemView, IssueItemView, ReceiveItemView, UpdateRestockView, FinishedItemsView

urlpatterns = [
    path('', DashboardView, name='dashboard'),
    path('all-items/', AllItemsView, name='all-items'),
    path('receive-history/', ReceiveHistoryView, name='receive-history'),
    path('issue-history/', IssueHistoryView, name='issue-history'),
    path('add-item/', AddItemView, name='add-item'),
    path('issue-item/', IssueItemView, name='issue-item'),
    path('receive-item/', ReceiveItemView, name='receive-item'),
    path('update-restock/<int:pk>/', UpdateRestockView, name='update-restock'),
    path('finished-items/', FinishedItemsView, name='finished-items')
]
 