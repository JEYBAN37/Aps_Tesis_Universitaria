# views.py
from rest_framework.response import Response
from rest_framework import status, generics
from aps_api.models.infoGeneral import InfoGeneral
from aps_api.models.pollster import Pollster
from aps_api.serializers.infoGeneralSerializer import InfoGeneralSerializer


def pollster_exists(pollster_id):
    return Pollster.objects.filter(serial_id=pollster_id).exists()


class SociambientalCreate (generics.CreateAPIView):
    queryset = InfoGeneral.objects.all()
    serializer_class = InfoGeneralSerializer

    def create(self, request, *args, **kwargs):
        pollster_id = request.data.get('pollster')
        print(pollster_id)
        try:
            pollster_id = int(request.data.get('pollster'))
        except ValueError:
            return Response({"Error": "ID de Encuestador no es un número entero válido"},
                            status=status.HTTP_400_BAD_REQUEST)

        if not pollster_exists(pollster_id):
            return Response({"error": f"El Encuestador con ID {pollster_id} no existe"},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
