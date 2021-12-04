from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from . import Serializer
from . import models


# @api_view(['GET', 'POST'])
@csrf_exempt
def index(request):
    if request.method == 'GET':
        sp = models.Simple_Product.objects.all()
        vp = models.Variety_Product.objects.all()
        SpSerializer = Serializer.SpSerliazer(sp, many=True)
        VpSerializer = Serializer.VpSerliazer(vp, many=True)
        var = SpSerializer.data, VpSerializer.data
        data = JsonResponse(var, safe=False)
    else:
        data = []
    return render(request, 'index.html', {'data': data})
