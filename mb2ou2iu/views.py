
from .models import Main_Content
from .serializers import MainContentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class MainContentList(APIView):
    def get(self, request):
        data = Main_Content.objects.all()
        serializer = MainContentSerializer(data, many=True)
        return Response(serializer.data)