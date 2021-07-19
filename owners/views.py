import json

from django.http import JsonResponse
from django.views import View

from owners.models import Owner, Dog



class OwnerRegister(View):
    def post(self, request):
        data = json.loads(request.body)

        owner = Owner.objects.create(
            name = data['name'],
            email = data['email'],
            age = data['age']
        )

        return JsonResponse({'Message':'CREATED'}, status=201)


class DogRegister(View):
    def post(self, request):
        data = json.loads(request.body)

        owner = Owner.objects.get(name=data['owner'])
        dog = Dog.objects.create(
            name = data['name'],
            age = data['age'],
            owner = owner
        )

        return JsonResponse({'Message':'CREATED'}, status=201)
