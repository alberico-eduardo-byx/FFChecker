from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class FeatureViewAPIView(APIView):
    """
    FeatureToggle.is_feature_active
    """
    def post(self, request):
        return Response(
            {'message': 'API Funcionando'},
            status=status.HTTP_200_OK,
        )
