from django.contrib import admin
from django.urls import path
from Proyecto1.views import saludo
from Proyecto1.views import segunda_vista
from Proyecto1.views import DiaDeHoy
from Proyecto1.views import nombre_persona
from Proyecto1.views import probando_template

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('saludo/',saludo),
    path ('segundavista/', segunda_vista),
    path ('diaDeHoy/', DiaDeHoy),
    path ('nombrepersona/<nombre>/', nombre_persona),
    path ('probandoTemplate/', probando_template)
]


