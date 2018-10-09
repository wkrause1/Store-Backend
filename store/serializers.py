from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id' ,'product_name' , 'product_description' , 'product_price' , 'product_image')

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.product_id = validated_data.get('id' , instance.id)
        instance.product_name = validated_data.get('product_name', instance.product_name)
        instance.product_description = validated_data('product_description' , instance.product_description)
        instance.product_price = validated_data('product_price' , instance.product_price)
        instance.save()
        return instance

