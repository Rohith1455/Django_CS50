from django.urls import path
from first_app import views

app_name="first_app"

urlpatterns = [
    path('hello',views.index,name='index'),
    path('brain',views.brain,name="brain"),
    path('david',views.david,name="david"),
    path('<str:name>',views.Greet,name="Greet"),   
]