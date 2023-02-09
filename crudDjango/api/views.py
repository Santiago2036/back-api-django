from django.shortcuts import render
from django.views import View
from .models import Company
from django.utils.decorators import method_decorator
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


class CompanyView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            companies = list(Company.objects.filter(id=id).values())

            if len(companies) > 0:
                datos = {"message": companies}
            else:
                datos = {"message": "not found"}
            return JsonResponse(datos)
        else:
            companies = list(Company.objects.values())

            if len(companies) > 0:
                datos = {"message": "success", "companies": companies}
            else:
                datos = {"message": "there are not data"}
            return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)

        Company.objects.create(
            name=jd["name"], website=jd["website"], foundation=jd["foundation"]
        )

        return JsonResponse({"message": "success"})

    def put(self, request, id):
        jd = json.loads(request.body)

        companies = Company.objects.filter(id=id).values()

        if len(companies) > 0:
            set_companies = Company.objects.get(id=id)
            set_companies.name = jd["name"]
            set_companies.foundation = jd["foundation"]
            set_companies.website = jd["website"]
            set_companies.save()

            datos = {"message ": "succesfull put"}
        else:
            datos = {"message": "Not found"}

        return JsonResponse(datos)

    def delete(self, request, id):
        companies = Company.objects.filter(id=id).values()

        if len(companies) > 0:
            companies = Company.objects.filter(id=id).delete()
            datos = {"message": "success"}
        else:
            datos = {"message": "Not found"}

        return JsonResponse(datos)
