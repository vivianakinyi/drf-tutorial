from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

@api_view(['GET','POST'])
def snippet_list(request, format=None):
	"""
	List all snippets or create a new snippet
	"""
	if request.method == 'GET':
		snippets = Snippet.objects.all()
		serializer = SnippetSerializer(snippets, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = SnippetSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serilaizer.data, status=status.HTTP_201_CREATED)
		return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)

#View for an individual snippet 

@api_view(['GET', 'PUT','DELETE'])
def snippet_detail(request, pk, format=None):
	try:
		snippet = Snippet.objects.get(pk=pk)
	except Snippet.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method =='GET':
		serializer = SnippetSerializer(snippet)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serilaizer = SnippetSerializer(snippet,data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		snippet.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)










#Introduction to Serializers (un refactored code)
# from django.shortcuts import render

# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer

# class JSONResponse(HttpResponse):
# 	"""
# 	An HttpResponse that renders its content into JSON.
# 	"""
# 	def __init__(self, data, **kwargs):
# 		content = JSONRenderer().render(data)
# 		kwargs['content_type'] = 'application/json'
# 		super(JSONResponse, self).___init__(content, **kwargs)

# @csrf_exempt
# def snippet_list(request):
# 	"""
# 	List all code snippet or create a new code
# 	"""
# 	if request.method == 'GET':
# 		snippets = Snippet.objects.all()
# 		serializer = SnippetSerializer(snippets, many=True)
# 		return JSONResponse(serializer.data)

# 	elif request.method == 'POST':
# 		data = JSONParser().parse(request)
# 		serilizer = SnippetSerializer(data=data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return JSONResponse(serilaizer.data, status=201)
# 		return JSONResponse(serializer.errors, status=400)

# @csrf_exempt
# def snippet_detail(request,pk):
# 	# """
# 	# Retrieve, update or delete a code snippets
# 	# """
# 	try: 
# 		snippet = Snippet.objects.get(pk=pk)
# 	except Snippet.DoesNotExist:
# 		return HttpResponse(status=404)

# 	if request.method == 'GET':
# 		serializer = SnippetSerializer(snippet)
# 		return JSONResponse(serilaizer.data)

# 	elif request.method == 'PUT':
# 		data = JSONParser().parse(request)
# 		serilaizer = SnippetSerializer(snippet, data=data)
# 		if serilizer.is_valid():
# 			serilizer.save()
# 			return JSONResponse(serilizer.data)
# 		return JSONResponse(serial.errors, status=400)

# 	elif request.method == 'DELETE':
# 		snippet.delete()
# 		return HttpResponse(status=204)

