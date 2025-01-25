from django.http.response import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from store.models import Product,Category,Cart,Order
from store.serializers import ProductSerializer,CategorySerializer,OrderSerializer,CartSerializer
from rest_framework import status
from django.db.models import Q


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_category(request):
    try:
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Successfully Created Category"},serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_categories(request,id):
    try:
        categories = Category.objects.get(id=id)
        serializer = CategorySerializer(categories)
        return Response({"message":"Categories Created successfully"})
    except Category:
        return Response({"error": "Categories Not Found,Server error"},serializer.data,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_product(request):
    try:
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": "Product Not Created"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_products(request):
    try:
        products = Product.objects.filter(is_available=True)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Product.DoesNotExist :
        return Response({"error":"Producted Not Found"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['GET'])
def list_products(request):
    search = request.query_params.get('search', None)
    category_id = request.query_params.get('category', None)
    price_lte = request.query_params.get('price__lte', None)
    
    products = Product.objects.all()

    if search:
        products = products.filter(Q(name_icontains=search) | Q(description_icontains=search))
    
    if category_id:
        products = products.filter(category_id=category_id)

    if price_lte:
        products = products.filter(price__lte=price_lte)
    
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
    

api_view(["POST"])
@permission_classes([IsAuthenticated])
def place_order(request):
    try:
        user = request.user
        cart = Cart.objects.get(user=user)

        if not cart.products.exists():
            raise Exception("Your cart is empty. Add products to your cart before placing an order.")

        payment_status = request.data.get("payment_status", "Pending")
        order_data = {
            "user": user.id,
            "cart": cart.id,
            "status": "Pending",
            "payment_status": payment_status
        }

        serializer = OrderSerializer(data=order_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "message": "Order placed successfully.",
            "order": serializer.data
        }, status=status.HTTP_201_CREATED)

    except Cart.DoesNotExist:
        return Response({"message": "Cart not found."}, status=status.HTTP_404_NOT_FOUND)
    