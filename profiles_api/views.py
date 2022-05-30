from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPIView(APIView):
    """Test API view"""
    
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_api_view = [
            'Uses HTTP methods as function (get, post, patch, put, delete...'
            
        ]
        
        return Response({'message': 'Hello!', 'an_api_view': an_api_view})