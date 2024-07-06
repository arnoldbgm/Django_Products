from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import ProductoSerializer
from .models import ProductoModel


class ProductPost(APIView):
    def post(self, req):
        serializer = ProductoSerializer(
            data=req.data, context={'request': req})
        if serializer.is_valid():
            serializer.save()
            return Response({
                'msg': 'Creacion exitosa',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, req):
        queryset = ProductoModel.objects.all()
        serializer = ProductoSerializer(
            queryset, context={'request': req}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductDeleteGet(APIView):
    def delete(self, req, id):
        queryset = ProductoModel.objects.get(id=id)
        serializer = ProductoSerializer(queryset)
        queryset.delete()
        return Response({
            'msg': f'Se elimino correctamente el registro {id}',
            'data': serializer.data
        })

    def get(self, req, id):
        queryset = ProductoModel.objects.get(id=id)
        serializer = ProductoSerializer(queryset,context={'request': req})
        return Response(serializer.data)

    def put(self, req, id):
        queryset = ProductoModel.objects.get(id=id)
        if (queryset == None):
            return Response(status=status.HTTP_200_OK, data={'error': 'Not found data'})
        serializer = ProductoSerializer(
            queryset, context={'request': req}, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
