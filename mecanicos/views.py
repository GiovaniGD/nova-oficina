from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from clientes.models import Cliente, Carro
import re
from django.core import serializers
import json
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

@login_required(login_url="/usuarios/login/")
def mecanicos(request):
    if request.method == "GET":
        mecanicos_list = Cliente.objects.all()
        return render(request, 'mecanicos.html', {'mecanicos': mecanicos_list})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')

        mecanico = Mecanico.objects.filter(cpf=cpf)

        if mecanico.exists():
            return render(request, 'mecanicos.html', { 'nome': nome, 'sobrenome': sobrenome, 'email': email })

        if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
            return render(request, 'mecanicos.html', { 'nome': nome, 'sobrenome': sobrenome, 'cpf': cpf })

        mecanico= Mecanico(
            nome = nome,
            sobrenome = sobrenome,
            email = email,
            cpf = cpf
        )

        mecanico.save()

        return render(request, 'mecanicos.html', {'nome': nome, 'sobrenome': sobrenome, 'cpf': cpf})

@login_required(login_url="/usuarios/login/")
def att_mecanico(request):
    id_mecanico = request.POST.get('id_mecanico')
    mecanico = Mecanico.objects.filter(id=id_mecanico)
    carros = Carro.objects.filter(mecanico=mecanico[0])
    mecanico_json = json.loads(serializers.serialize('json', mecanico))[0]['fields']
    mecanico_id = json.loads(serializers.serialize('json', mecanico))[0]['pk']
    carros_json = json.loads(serializers.serialize('json', carros))
    carros_json = [{'fields': i['fields'], 'id': i['pk']} for i in carros_json]
    data = {'mecanico': mecanico_json, 'carros': carros_json, 'mecanico_id': mecanico_id}
    return JsonResponse(data)


@login_required(login_url="/usuarios/login/")
def update_mecanico(request, id):
    body = json.loads(request.body)

    nome = body['nome']
    sobrenome = body['sobrenome']
    email = body['email']
    cpf = body['cpf']

    mecanico = get_object_or_404(Cliente, id=id)
    try:
        cliente.nome = nome
        cliente.sobrenome = sobrenome
        cliente.email = email
        cliente.cpf = cpf
        cliente.save()
        return JsonResponse({'status': '200', 'nome': nome, 'sobrenome': sobrenome, 'email': email, 'cpf': cpf})
    except:
        return JsonResponse({'status': '500'})
