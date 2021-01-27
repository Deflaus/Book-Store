from .models import Order
from .serializers import OrderSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import order_created


class OrderView(APIView):
    '''
    Представление для добавления заказа книги
    '''

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save(user=request.user)
            
            order_created.delay(obj.id)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
