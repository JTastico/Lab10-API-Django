from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Serie, Producto, Categoria
from .serializers import SerieSerializer
from rest_framework import generics
from .serializers import CategoriaSerializer
from .serializers import ProductoSerializer

class IndexView(APIView):
    def get(self, request):
        context = {'mensaje': 'servidor activo'}
        return Response(context)

class SeriesView(APIView):
    def get(self, request):
        dataSeries = Serie.objects.all()
        serSeries = SerieSerializer(dataSeries, many=True)
        return Response(serSeries.data)

    def post(self, request):
        serSerie = SerieSerializer(data=request.data)
        serSerie.is_valid(raise_exception=True)
        serSerie.save()
        return Response(serSerie.data)

class SerieDetailView(APIView):
    def get(self, request, serie_id):
        dataSerie = Serie.objects.get(pk=serie_id)
        serSerie = SerieSerializer(dataSerie)
        return Response(serSerie.data)

    def put(self, request, serie_id):
        dataSerie = Serie.objects.get(pk=serie_id)
        serSerie = SerieSerializer(dataSerie, data=request.data)
        serSerie.is_valid(raise_exception=True)
        serSerie.save()
        return Response(serSerie.data)

    def delete(self, request, serie_id):
        dataSerie = Serie.objects.get(pk=serie_id)
        dataSerie.delete()
        return Response({'mensaje': 'Serie eliminada'})


# Vistas para Categoría

class CategoriaListCreateView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

# Vistas para Producto
class ProductoListCreateView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer