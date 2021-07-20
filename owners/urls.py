#from wecode23.crud2.crud2.owners.views import GetDogOwner
from django.urls import path

from owners.views import *

urlpatterns = [
	path('owners', OwnerRegister.as_view()),
    path('dogs', DogRegister.as_view()),
    path('getdog', GetDogs.as_view()),
    path('getowner', GetOwners.as_view()),
    path('getdogowner', GetDogOwner.as_view()),
]
