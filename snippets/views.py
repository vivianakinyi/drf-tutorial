from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from snippets.serializers import UserSerializer
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import detail_route


#Creating an endpoint for the root of our API
@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })

#The UserList and UserDetail is refactored to one single viewset Userviewset below
#**********************************************************************************
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#The refactored class UserViewset 
class UserViewSet(viewsets.ReadOnlyModelViewSet):
	"""This automatically provides list and detail action"""
	queryset = User.objects.all()
	serializer_class = UserSerializer

#This viewset automatically provides CRUD actions and an extra highlight action
class SnippetViewSet(viewsets.ModelViewSet):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)

	@detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
	def highlight(self, request, *args, **kwargs):
		snippet = self.get_object()
		return Response(snippet.highlighted)

	def perform_create(self, serializer):
		serilaizer.save(owner=self.request.user)


#The SnippetList SnippetDetail and SnippetHighlight classes are then refactored to a single class SnippetViewSet above
#**********************************************************************************************************************
# class SnippetList(generics.ListCreateAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
#     #Added a .perform_create() method to associate snippet with users.
#     def perform_create(self, serializer):
#     	serializer.save(owner=self.request.user)


# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

# 	#Endpoints for the highlighted snippets
# class SnippetHighlight(generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     renderer_classes = (renderers.StaticHTMLRenderer,)

#     def get(self, request, *args, **kwargs):
#         snippet = self.get_object()
#         return Response(snippet.highlighted)

#Class based views with mixins

# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
# from rest_framework import mixins
# from rest_framework import generics

# class SnippetList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
# 	def get(self, request, *args, **kwargs):
# 		return self.list(request, *args, **kwargs)

# 	def put(self, request, *args, **kwargs):
# 		return self.update(request, *args, **kwargs)

# 	def delete(self, request, *args, **kwargs):
# 		return self.destroy(request, *args, **kwargs)


#Use of mixins to reuse


# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# 



#Class based views

# class SnippetList(APIView):
# 	"""
# 	List all snippets or create a new snippet
# 	"""
# 	def get(self, request, format=None):
# 		snippets = Snippet.objects.all()
# 		serializer = SnippetSerializer(snippets, many=True)
# 		return Response(serializer.data)

# 	def post(self, request, format=None):
# 		serializers = SnippetSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)

# class SnippetDetail(APIView):
# 	def get_object(self, pk):
# 		try:
# 			return Snippet.objects.get(pk=pk)
# 		except Snippet.DoesNotExist:
# 			raise Http404

# 	def get(self, request, pk, format=None):
# 		snippet = self.get_object(pk)
# 		serializer = SnippetSerializer(snippet)
# 		return Response(serializer.data)

# 	def put(self, request, pk, format=None):
# 		snippet = self.get_object(pk)
# 		serializer = SnippetSerializer(snippet, data=request.data)
# 		if serializer.is_valid():
# 			return Response(serializer.data)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 	def delete(self, request, pk, format=None):
# 		snippet = serializer.get_object(pk)
# 		snippet.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)



#Function-based views

# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer

# @api_view(['GET','POST'])
# def snippet_list(request, format=None):
# 	"""
# 	List all snippets or create a new snippet
# 	"""
# 	if request.method == 'GET':
# 		snippets = Snippet.objects.all()
# 		serializer = SnippetSerializer(snippets, many=True)
# 		return Response(serializer.data)

# 	elif request.method == 'POST':
# 		serializer = SnippetSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serilaizer.data, status=status.HTTP_201_CREATED)
# 		return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)

# #View for an individual snippet 

# @api_view(['GET', 'PUT','DELETE'])
# def snippet_detail(request, pk, format=None):
# 	try:
# 		snippet = Snippet.objects.get(pk=pk)
# 	except Snippet.DoesNotExist:
# 		return Response(status=status.HTTP_404_NOT_FOUND)

# 	if request.method =='GET':
# 		serializer = SnippetSerializer(snippet)
# 		return Response(serializer.data)

# 	elif request.method == 'PUT':
# 		serilaizer = SnippetSerializer(snippet,data = request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)

# 	elif request.method == 'DELETE':
# 		snippet.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)










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

