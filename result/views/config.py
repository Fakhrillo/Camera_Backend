from ..models import ConfigParameter
from rest_framework.views import APIView
from ..serializers import ConfigSerializer
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, UpdateAPIView

from rest_framework_simplejwt.authentication import  JWTAuthentication
from rest_framework.permissions import IsAdminUser


class ConfigurationPostAPIView(APIView):
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = ConfigSerializer
    
    def post(self, request, *args, **kwargs):
        data = request.data
        Cam_MxID = data.get('Cam_MxID')
        config = ConfigParameter.objects.filter(Cam_MxID=Cam_MxID).first()
        if config:
            serialized = self.serializer_class(config, data=data, partial=True)
            if serialized.is_valid():
                serialized.save()
            else:
                return Response(serialized.errors, status=400)
        else:
            serialized = self.serializer_class(data=data)
            if serialized.is_valid():
                serialized.save()
            else:
                return Response(serialized.errors, status=400)
        
        return Response({"detail":"configurations saved successfully"})


class GetConfigurationsAPIView(RetrieveAPIView):

    serializer_class = ConfigSerializer
    queryset = ConfigParameter.objects.all()

    lookup_field = 'Cam_MxID'
    

class UpdateConfigAPIView(UpdateAPIView):
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = ConfigSerializer
    queryset = ConfigParameter.objects.all()

    lookup_field = 'Cam_MxID'