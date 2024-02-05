from ..models import Tracked
from rest_framework.views import APIView
from ..serializers import ResultSerializer
from rest_framework.response import Response 
from rest_framework.generics import  CreateAPIView

from rest_framework_simplejwt.authentication import  JWTAuthentication
from rest_framework.permissions import IsAdminUser

class TrackedCreateAPIView(CreateAPIView):
    serializer_class = ResultSerializer
    queryset = Tracked.objects.all()


class GetTrackedAPIView(APIView):
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

    def get(self, request, *args, **kwargs):
        Cam_MxID = self.kwargs.get('Cam_MxID')
        data = Tracked.objects.filter(Cam_MxID=Cam_MxID).order_by('-id')
        serializer = ResultSerializer(data, many=True)
        return Response(serializer.data)
        
        

