from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """Test api view"""
    def get(self,request,format=None):
        """Return list of APIView Result"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch,put, delete)',
            'Is similar to django APIView',
            'Gives the most control over the api logic',
            'Is mapped manually to URL',
        ]
        
        return Response({'message': 'Hello','an_apiview':an_apiview})