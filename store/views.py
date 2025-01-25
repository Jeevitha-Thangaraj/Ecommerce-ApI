from django.http.response import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from store.models import Product,Category,Cart,Order
from store.serializers import ProductSerializer,CategorySerializer,OrderSerializer,CartSerializer
from rest_framework import status
from django.db.models import Q


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def product_catalog(request):
    products = Product.objects.all()

    # Filter by category
    category_id = request.GET.get('category')
    if category_id:
        products = products.filter(category_id=category_id)

    # Search by product name
    search_query = request.GET.get('search')
    if search_query:
        products = products.filter(name__icontains=search_query)

    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    serializer = CartSerializer(cart_items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request):
    product_id = request.data.get('product_id')
    quantity = request.data.get('quantity', 1)

    try:
        product = Product.objects.get(id=product_id)
        cart_item, created = Cart.objects.get_or_create(
            user=request.user, 
            product=product,
            defaults={'quantity': quantity}
        )
        if not created:
            cart_item.quantity += int(quantity)
            cart_item.save()

        serializer = CartSerializer(cart_item)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=404)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_from_cart(request):
    product_id = request.data.get('product_id')

    Cart.objects.filter(user=request.user, product_id=product_id).delete()
    return Response({'message': 'Item removed from cart'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_orders(request):
    orders = Order.objects.filter(user=request.user)
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_from_cart(request):
    product_id = request.data.get('product_id')

    Cart.objects.filter(user=request.user, product_id=product_id).delete()
    return Response({'message': 'Item removed from cart'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def place_order(request):
    cart_items = Cart.objects.filter(user=request.user)
    if not cart_items:
        return Response({'error': 'Cart is empty'}, status=400)

    total_amount = sum(item.product.price * item.quantity for item in cart_items)
    order = Order.objects.create(user=request.user, total_amount=total_amount)

    # Clear the cart after placing the order
    cart_items.delete()

    serializer = OrderSerializer(order)
    return Response(serializer.data)
