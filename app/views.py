from django.http import HttpResponse
from rest_framework.response import Response
from .serializers import BookSerializer
from .models import Book
import logging
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
# from .models import Product
# from .serializers import ProductSerializer

@swagger_auto_schema(method='POST', request_body=BookSerializer)
@api_view(['POST'])
def create_product(request):
    if request.method == 'POST':
        create_product = ProductSerializer(data=request.data)
        if create_product.is_valid():
            title = create_product.validated_data.get('title')
            description = create_product.validated_data.get('description')
            product = Product.objects.create(title=title, description=description)
            product.save()
            return Response(create_product.data, status=status.HTTP_201_CREATED)
        else:
            return Response(create_product.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"Error": "Invalid request type"}, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='GET')
@api_view(['GET'])
def read_product(request):
    if request.method == 'GET':
        all_products = Product.objects.all()
        serialized_products = ProductSerializer(all_products, many=True)
        return Response(serialized_products.data,    status=status.HTTP_200_OK)
    else:
        return Response(serialized_products.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def update_product(request, id):
    if request.method == 'PATCH':
        try:
            product = Product.objects.get(id=id)
            update_seriailizer = UpdateProductSerializer(product, data=request.data, partial=True)
            if update_serializer.is_valid():
                update_serializer.save()
                return Response({"Message": "Product updated"}, status=status.HTTP_200_OK)
            else:
                 return Response(update_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"Error": f"Unexpected error {e} occurred."}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"Error": "Invalid request type"}, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='DELETE', request_body=BookSerializer)
@api_view(['DELETE'])
def delete_view(request):
    if request.method == 'DELETE':
        all_products = Product.objects.all()
        all_product.delete()
        return Response({"Message": "All Products have been deleted"}, status=status.HTTP_200_OK)
    else:
        return Response({"Error": "Invalid request type"}, status=status.HTTP_400_BAD_REQUEST)



# def mainmenu(request):
#     return HttpResponse("Hello world")


# @swagger_auto_schema(method='GET', response={200: BookSerializer(many=True)})
# @api_view(['GET', 'POST'])
# def books(request):
#     if request.method == 'GET':
#         books = Book.objects.all()
#         context = BookSerializer(books, many=True)
#         return Response(context.data)
#     if request.method == 'POST':
#         context = BookSerializer(data=request.data)
#         if context.is_valid():
#             context.save()
#             return Response(context.data, status=status.HTTP_201_CREATED)
#         return Response(context.errors, status=status.HTTP_400_BAD_REQUEST)

# # @swaggen_auto_schema(method='POST', request_body=BookSerializer, response={201: BookSerializer()})

# @api_view(['GET', 'PUT', 'DELETE'])
# def book_detail(request, id):
#     if request.method == 'GET':
#         book = get_object_or_404(Book, id=id)
#         serializer = BookSerializer(book)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         book = get_object_or_404(Book, id=id)
#         serializer = BookSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         book = get_object_or_404(Book, id=id)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# # # Create your views here.
