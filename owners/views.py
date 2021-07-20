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

class GetOwners(View):
    def get(self, request):
        owners = Owner.objects.all()
        results=[]
        for owner in owners:
            results.append(
                {
                    "name" : owner.name,
                    "email": owner.email,
                    "age"  : owner.age
                }
            )
        return JsonResponse({'resutls':results}, status=200)

class GetDogs(View):
    def get(self, request):
        dogs = Dog.objects.all()
        results=[]
        for dog in dogs:
            results.append(
                {
                    "name"   : dog.name,
                    "age"    : dog.age,
                    "owner"  : dog.owner.name
                }
            )
        return JsonResponse({'resutls':results}, status=200)

class GetDogOwner(View):
    def get(self, request):
        owners = Owner.objects.all()
        results=[]

        for owner in owners:
            list= []
            for dog in Dog.objects.filter(owner = owner).values('name', 'age'):
                list.append(dog)
            results.append(
                {
                    "name" : owner.name,
                    "age"  : owner.age,
                    "dogs" : list
                }
            )
        
        return JsonResponse({'resutls':results}, status=200)
    


