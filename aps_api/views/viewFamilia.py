from rest_framework.decorators import api_view
from rest_framework.response import Response
from aps_api.models.family import Family
from aps_api.serializers.familySerializer import FamilySerializer
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework import status


@api_view(['POST'])
def add_items(request):
    item = FamilySerializer(data=request.data)
    if Family.objects.filter(**request.data).exists():
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
        serial_id = request.query_params.get('serial_id')

        if info_general is not None:
            info_general = int(info_general)
            items = Family.objects.filter(info_general=info_general)
        elif serial_id is not None:
            serial_id = int(serial_id)
            items = Family.objects.filter(serial_id=serial_id)
        elif info_general is None and serial_id is None:
            items = Family.objects.all()
        else:
            return Response({"Error": "No se puede encontrar el registro"}, status=status.HTTP_404_NOT_FOUND)

        if items:
            serializer = FamilySerializer(items, many=True)
            return Response(serializer.data)
        else:
            return Response({"Error": "No existe registros"}, status=status.HTTP_404_NOT_FOUND)

    except ValueError:
        return Response({"Error": "Accion ilegal en el sistema"},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def update_items(request, serial_id):
    item = Family.objects.get(serial_id=serial_id)
    data = FamilySerializer(instance=item, data=request.data)

    if data.is_valid():
        data.save()
        return Response({"El formulario se actulizo correctamente"}, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_items(request, serial_id):
    item = get_object_or_404(Family, serial_id=serial_id)
    item.delete()
    return Response({"Eliminado exitosamente ", serial_id}, status=status.HTTP_202_ACCEPTED)
