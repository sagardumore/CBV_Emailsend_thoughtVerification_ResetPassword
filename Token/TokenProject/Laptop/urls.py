from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.AddLaptopView.as_view(),name='add_laptop'),
    path('show/',views.ShowLaptopView.as_view(),name='show_laptop'),
    path('update/<int:i>/',views.LaptopUpdateView.as_view(),name='update_laptop'),
    path('delete/<int:i>/',views.LaptopDeleteView.as_view(),name='delete_laptop')
]