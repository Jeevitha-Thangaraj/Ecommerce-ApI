from rest_framework import serializers
from store.models import Product,Category,User,Cart,Order

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  # This will include all fields from the model

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        field="__all__"

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        field="__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        field="__all__"









# class CartSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Cart
#         field="__all__"

# class CartItemtSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=CartItem
#         field="__all__"

# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Order
#         field="__all__"
