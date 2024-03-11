from ..models import Tracked
from rest_framework.views import APIView
from ..serializers import ResultSerializer
from rest_framework.response import Response 
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.generics import  CreateAPIView

from datetime import datetime, timedelta
from django.utils import timezone

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
        
        start_date_str = request.query_params.get('start_date')
        end_date_str = request.query_params.get('end_date')

        if not (start_date_str and end_date_str):
            today = timezone.now().date()
            start_date = datetime.combine(today, datetime.min.time())
            end_date = datetime.combine(today, datetime.max.time())
        else:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d') + timedelta(days=1)

        data = Tracked.objects.filter(Cam_MxID=Cam_MxID, created_at__range=(start_date, end_date)).order_by('-id')
        
        serializer = ResultSerializer(data, many=True)
        return Response(serializer.data)
        

class GetLastTrackedAPIView(APIView):
    def get(self, request, *args, **kwargs):
        Cam_MxID = request.query_params.get('Cam_MxID')

        if not Cam_MxID:
            return Response({'error': 'Missing Cam_MxID parameter'}, status=HTTP_400_BAD_REQUEST)

        try:
            last_tracked_object = Tracked.objects.filter(Cam_MxID=Cam_MxID).latest('created_at')
        except:
            return Response({'error': 'No tracked object found for Cam_MxID: {}'.format(Cam_MxID)}, status=HTTP_404_NOT_FOUND)

        data = ResultSerializer(last_tracked_object).data

        return Response(data)