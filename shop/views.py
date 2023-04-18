from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.generics import (ListCreateAPIView, RetrieveDestroyAPIView,
                                     RetrieveUpdateAPIView)
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from .models import Product
from .permissions import IsAdminOrReadOnly
from .serializers import ProductSerializer


class ShopAPIList(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ShopAPIUpdate(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)


class ShopAPIDestroy(RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly,)
    

# class ShopViewSet(ModelViewSet):
#     serializer_class = ProductSerializer

#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
        
#         if not pk:
#             return Product.objects.all()[:3]
        
#         return Product.objects.filter(pk=pk)
        
#     @action(methods=['get'], detail=True)
#     def title(self, request, pk):
#         title = Product.objects.get(pk=pk)
#         return Response({'title': title.title})
