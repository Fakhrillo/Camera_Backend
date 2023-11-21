from ..models import ConfigParameter
from rest_framework.views import APIView
from ..serializers import ConfigSerializer
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, UpdateAPIView



class ConfigurationPostAPIView(APIView):
    serializer_class = ConfigSerializer
    
    def post(self, request, *args, **kwargs):
        data = request.data
        mxid = data.get('mxid')
        config = ConfigParameter.objects.filter(mxid=mxid).first()
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

    lookup_field = 'mxid'
    

class UpdateConfigAPIView(UpdateAPIView):
    serializer_class = ConfigSerializer
    queryset = ConfigParameter.objects.all()

    lookup_field = 'mxid'