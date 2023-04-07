from django.contrib import admin
from django.urls import path
from raffle_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', raffle_list, name='raffle_list'),
    path('raffle/<int:raffle_id>/', raffle_detail, name='raffle_detail'),
]
