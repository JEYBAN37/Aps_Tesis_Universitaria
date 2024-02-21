from rest_framework.decorators import api_view
from rest_framework.response import Response
from aps_api.models.sanation import Sanation
from aps_api.serializers.sanationSerializer import SanationSerializer
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework import status


@api_view(['POST'])
def add_items(request):
    item = SanationSerializer(data=request.data)
    if Sanation.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if item.is_valid():
        item.save()
        return Response(item.data, status=status.HTTP_201_CREATED)
    else:
        return Response(item.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def view_items(request):
    try:
        housing = request.query_params.get('housing')
        serial_id = request.query_params.get('serial_id')

        if housing is not None:
            housing = int(housing)
            items = Sanation.objects.filter(housing=housing)
        elif serial_id is not None:
            serial_id = int(serial_id)
            items = Sanation.objects.filter(serial_id=serial_id)
        elif housing is None and serial_id is None:
            items = Sanation.objects.all()
        else:
            return Response({"Error": "No se puede encontrar el registro"}, status=status.HTTP_404_NOT_FOUND)

        if items:
            serializer = SanationSerializer(items, many=True)
            return Response(serializer.data)
        else:
            return Response({"Error": "No existe registros"}, status=status.HTTP_404_NOT_FOUND)

    except ValueError:
        return Response({"Error": "Accion ilegal en el sistema"},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def update_items(request, serial_id):
    item = Sanation.objects.get(serial_id=serial_id)
    data = SanationSerializer(instance=item, data=request.data)

    if data.is_valid():
        data.save()
        return Response({"El formulario se actulizo correctamente"}, status=status.HTTP_200_OK)
    else:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_items(request, serial_id):
    item = get_object_or_404(Sanation, serial_id=serial_id)
    item.delete()
    return Response({"Eliminado exitosamente ", serial_id}, status=status.HTTP_202_ACCEPTED)
