from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers.pollsterSerializer import PollsterSerializer  # Corrige el nombre del serializador
from .models.pollster import Pollster


class Viewpollster(APIView):

    def get(self, request):
        queryset = Pollster.objects.all()
        serializer = PollsterSerializer(queryset, many=True)  # Corrige el nombre del serializador
        return Response(serializer.data)

    def post(self, request):
        serializer = PollsterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
