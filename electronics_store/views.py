from rest_framework import permissions, viewsets

from .models import NetworkNode, Product
from .serializers import NetworkNodeSerializer, ProductSerializer


# Create your views here.
class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        if "debt" in serializer.validated_data:
            serializer.validated_data.pop("debt")
        super().perform_update(serializer)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
