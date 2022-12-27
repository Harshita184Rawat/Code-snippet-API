from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from djrest.models import djrest
from snippets.serializers import SnippetSerializer

# Create your views here.

@csrf_exempt
def djrest_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        djrest = djrest.objects.all()
        serializer = djrestSerializer(djrest, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
@csrf_exempt
def djrest_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        djrest = djrest.objects.get(pk=pk)
    except djrest.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(djrest)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = djrestSerializer(djrest, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        djrest.delete()
        return HttpResponse(status=204)