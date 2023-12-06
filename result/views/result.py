from ..models import Tracked
from rest_framework.views import APIView
from ..serializers import ResultSerializer
from rest_framework.response import Response 
from rest_framework.generics import  CreateAPIView
# Create your views here.



class TrackedCreateAPIView(CreateAPIView):
    serializer_class = ResultSerializer
    queryset = Tracked.objects.all()


class GetTrackedAPIView(APIView):
    def get(self, request, *args, **kwargs):
        Cam_MxID = self.kwargs.get('Cam_MxID')
        data = Tracked.objects.filter(Cam_MxID=Cam_MxID).order_by('-id')
        serializer = ResultSerializer(data, many=True)
        return Response(serializer.data)
        
        

