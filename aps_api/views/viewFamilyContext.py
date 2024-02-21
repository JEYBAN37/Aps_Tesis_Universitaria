from rest_framework.decorators import api_view
from rest_framework.response import Response
from aps_api.models.familyContext import FamilyContext
from aps_api.serializers.familyContextSerializer import FamilyContextSerializer
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework import status


@api_view(['POST'])
def add_items(request):
    item = FamilyContextSerializer(data=request.data)
    if FamilyContext.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if item.is_valid():
        item.save()
        return Response(item.data, status=status.HTTP_201_CREATED)
    else:
        return Response(item.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def view_items(request):
    try:
        family = request.query_params.get('family')
        serial_id = request.query_params.get('serial_id')

        if family is not None:
            family = int(family)
            items = FamilyContext.objects.filter(family=family)
        elif serial_id is not None:
            serial_id = int(serial_id)
            items = FamilyContext.objects.filter(serial_id=serial_id)
        elif family is None and serial_id is None:
            items = FamilyContext.objects.all()
        else:
            return Response({"Error": "No se puede encontrar el registro"}, status=status.HTTP_404_NOT_FOUND)

        if items:
            serializer = FamilyContextSerializer(items, many=True)
            return Response(serializer.data)
        else:
            return Response({"Error": "No existe registros"}, status=status.HTTP_404_NOT_FOUND)

    except ValueError:
        return Response({"Error": "Accion ilegal en el sistema"},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def update_items(request, serial_id):
    item = FamilyContext.objects.get(serial_id=serial_id)
    data = FamilyContextSerializer(instance=item, data=request.data)

    if data.is_valid():
        data.save()
        return Response({"El formulario se actulizo correctamente"}, status=status.HTTP_200_OK)
    else:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_items(request, serial_id):
    item = get_object_or_404(FamilyContext, serial_id=serial_id)
    item.delete()
    return Response({"Eliminado exitosamente ", serial_id}, status=status.HTTP_202_ACCEPTED)
