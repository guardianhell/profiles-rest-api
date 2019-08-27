from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        an_apiview = [
            'adadadaddwa',
            'dwdadwadaddaw',
            'dwadawdwdaw',
        ]
        return Response({'Message:': 'Hello', 'an_api : ': an_apiview})
