# This takes serialized/not serialized data and renders it as json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer
@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    # Serializing the data before returning it
    # many is saying we're serializing multiple items, we have 4 in the database
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data = request.data)
    serializer.save() if serializer.is_valid() else "error"
    return Response(serializer.data)