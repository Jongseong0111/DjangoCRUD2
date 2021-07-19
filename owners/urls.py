from django.urls import path

from owners.views import OwnerRegister, DogRegister

urlpatterns = [
	path('', OwnerRegister.as_view()),
    path('dogs', DogRegister.as_view()),
]
