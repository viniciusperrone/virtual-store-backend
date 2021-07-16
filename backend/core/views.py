from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Products
from .serializers import ProductsSerialize

# Create your views here.
@csrf_exempt
def ProductsApi(request, id=0):
    if request.method=='GET':   
        products = Products.objects.all()
        products_serializer = ProductsSerialize( products, many=True)
        return JsonResponse(products_serializer.data , safe=False)
        
    elif request.method=='POST':
        product_data = JSONParser().parse(request)
        product_serializer = ProductsSerialize(data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse("Successfully added product!!", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    elif request.method=='PUT':
        product_data = JSONParser().parse(request)
        product = Products.objects.get(id=product_data['id'])
        product_serializer = ProductsSerialize(product, data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update!!", safe=False)

    elif request.method=='DELETE':
        product = Products.objects.get(id=id)
        product.delete()
        return JsonResponse("Deleted Succefully", safe=False)
    


# successfully added product