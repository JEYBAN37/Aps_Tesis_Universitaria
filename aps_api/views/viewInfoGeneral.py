from wsgiref import headers
# views.py
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from aps_api.models.pollster import Pollster
from aps_api.models.infoGeneral import InfoGeneral
from aps_api.serializers.infoGeneralSerializer import InfoGeneralSerializer
from rest_framework import serializers
from rest_framework import status


def pollster_exists(pollster_id):
    return Pollster.objects.filter(serial_id=pollster_id).exists()


@api_view(['POST'])
def add_items(request):
    item = InfoGeneralSerializer(data=request.data)
    pollster_id = request.data.get('pollster')
    try:
        pollster_id = int(pollster_id)
    except ValueError:
        return Response(item.errors, status=status.HTTP_400_BAD_REQUEST)

    if not pollster_exists(pollster_id):
        return Response(item.errors, status=status.HTTP_400_BAD_REQUEST)
    if InfoGeneral.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if item.is_valid():
        item.save()
        return Response(item.data, status=status.HTTP_201_CREATED)
    else:
        return Response(item.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def view_items(request):
    try:
        pollster_id = request.query_params.get('pollster')
        print(pollster_id)
        if pollster_id is not None and pollster_id is not pollster_exists(pollster_id):
            pollster_id = int(pollster_id)
            items = InfoGeneral.objects.filter(pollster=int(pollster_id))
        elif pollster_id is None:
            items = InfoGeneral.objects.all()
        else:
            return Response({"Error": "No se puede encontrar el registro"}, status=status.HTTP_404_NOT_FOUND)

        if items:
            serializer = InfoGeneralSerializer(items, many=True)
            return Response(serializer.data)
        else:
            return Response({"Error": "No existe registros"}, status=status.HTTP_404_NOT_FOUND)

    except ValueError:
        return Response({"Error": "Accion ilegal en el sistema"},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def update_items(request, serial_id):
    item = InfoGeneral.objects.get(serial_id=serial_id)
    data = InfoGeneralSerializer(instance=item, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_items(request, serial_id):
    item = get_object_or_404(InfoGeneral, serial_id=serial_id)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)







