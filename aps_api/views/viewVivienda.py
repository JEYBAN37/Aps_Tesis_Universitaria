from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from aps_api.models.housing import Housing
from aps_api.models.infoGeneral import InfoGeneral
from aps_api.serializers.housingSerializer import HousingSerializer
from rest_framework import serializers
from rest_framework import status


def info_general_exists(info_general):
    return InfoGeneral.objects.filter(serial_id=info_general).exists()


@api_view(['POST'])
def add_items(request):
    item = HousingSerializer(data=request.data)

    if Housing.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if item.is_valid():
        item.save()
        return Response(item.data, status=status.HTTP_201_CREATED)
    else:
        return Response(item.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def view_items(request):
    try:
        info_general = request.query_params.get('info_general')
        if info_general is not None:
            info_general = int(info_general)
            items = Housing.objects.filter(info_general=int(info_general))
        elif info_general is None:
            items = Housing.objects.all()
        else:
            return Response({"Error": "No se puede encontrar el registro"}, status=status.HTTP_404_NOT_FOUND)

        if items:
            serializer = HousingSerializer(items, many=True)
            return Response(serializer.data)
        else:
            return Response({"Error": "No existe registros"}, status=status.HTTP_404_NOT_FOUND)

    except ValueError:
        return Response({"Error": "Accion ilegal en el sistema"},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def update_items(request, serial_id):
    item = Housing.objects.get(serial_id=serial_id)
    data = HousingSerializer(instance=item, data=request.data)

    if data.is_valid():
        data.save()
        return Response({"El formulario se actulizo correctamente"}, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_items(request, serial_id):
    item = get_object_or_404(Housing, serial_id=serial_id)
    item.delete()
    return Response({"Eliminado exitosamente ", serial_id}, status=status.HTTP_202_ACCEPTED)
