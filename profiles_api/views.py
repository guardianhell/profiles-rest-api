from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets


class HelloApiView(APIView):
    """Test API View"""
    serializers_class = serializers.HelloSerializer

    def get(self, request, format=None):
        an_apiview = [
            'adadadaddwa',
            'dwdadwadaddaw',
            'dwadawdwdaw',
        ]
        return Response({'Message:': 'Hello', 'an_api : ': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializers_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        # return Response({'Method': 'POST'})

    def put(self, request, pk=None):
        """handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API View Sets"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        a_viewset = [
            'view set action this particular update',
            'automaticaly maps to urls using krouters',
            'provides more funcionality with less code'
        ]
        return Response({'message:': 'Hello', 'a_view': a_viewset})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'Message ': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        return Response({'http_method': 'DELETE'})
