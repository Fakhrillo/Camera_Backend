import boto3
from django.conf import settings
from ..models import StreamPhoto
from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import StreamPhotoSerializer
from django.utils import timezone

class StreamPhotoUpdateView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        Cam_MxID=self.kwargs.get('Cam_MxID')   
        try:
            camera = StreamPhoto.objects.get(Cam_MxID=Cam_MxID)
            serializer = StreamPhotoSerializer(instance=camera, data=data, partial=True)
            if serializer.is_valid():
                serializer.save(posted_on=timezone.now())
                return Response({'detail':'Updated successfully'}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            dt = {
                'image': data['image'],
                'Cam_MxID': Cam_MxID,
            }
            serializer = StreamPhotoSerializer(data=dt)
            if serializer.is_valid():
                serializer.save()
                return Response({'detail':'Added  successfully'}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        Cam_MxID = self.kwargs.get('Cam_MxID')
        camera = StreamPhoto.objects.get(Cam_MxID=Cam_MxID)
        serialized = StreamPhotoSerializer(camera)
        return Response(serialized.data)
 
 
def get_image_urls(request):
    # Initialize the S3 client
    s3_client = boto3.client('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID, 
                             aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,)
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME

    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name)

        # Check if the objects are found in the bucket
        if 'Contents' in response:
            image_urls = []
            for obj in response['Contents']:
                image_url = f"https://{settings.AWS_S3_CUSTOM_DOMAIN}/{obj['Key']}"
                image_urls.append(image_url)
            return render(request, 'image_urls.html', {'image_urls': image_urls}) 
        else:
            return render(request, 'image_urls.html', {'message': 'No images found in the bucket.'})
    except Exception as e:
        return render(request, 'image_urls.html', {'error': str(e)})
    