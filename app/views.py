from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class FeatureViewAPIView(APIView):
    """
    FeatureToggle.is_feature_active
    """
    def post(self, request):
        """
        FeatureToggle.is_feature_active
        """
        return Response(
            {'message': 'API Funcionando'},
            status=status.HTTP_200_OK,
        )

    def delete(self, request):
        return Response(
            {'message': 'API Funcionando'},
            status=status.HTTP_200_OK,
        )

    def get(self, request):
        """
        Feature
        Toggle
        is_feature_active
        FeatureToggle.is_feature_active
        """
        return Response(
            {'message': 'API Funcionando'},
            status=status.HTTP_200_OK,
        )
    
    def put(self, request):
        """
        aaaa
        FeatureToggle.is_feature_active('Alberico')
        """
        return Response(
            {'message': 'API Funcionando'},
            status=status.HTTP_200_OK,
        )
