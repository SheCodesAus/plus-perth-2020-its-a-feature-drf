from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Transaction, Bucket, Icon
from .serializers import TransactionSerializer, BucketSerializer, IconSerializer

# Create your views here.
class TransactionList(APIView):

    # Add permission classes here!!!

    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )