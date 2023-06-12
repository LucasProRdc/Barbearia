from django.urls import path
from .views import customer_list, customer_new, customer_update, customer_delete

urlpatterns = [
    path('list/', customer_list, name="customer_list"),
    path('new/', customer_new, name="customer_new"),
    path('update/<int:id>/', customer_update, name="customer_update"),
    path('delete/<int:id>/', customer_delete, name="customer_delete")
]
    