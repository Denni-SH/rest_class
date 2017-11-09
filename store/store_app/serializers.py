from rest_framework.serializers import ModelSerializer
from .models import Product, Category


class ProductsSerializers(ModelSerializer):
    class Meta:
        model = Product
        # fields = ('pk',)
        fields = '__all__'


class CategorySerializers(ModelSerializer):
    # products = ProductsSerializers(many=True)
    class Meta:
        model = Category
        fields = '__all__'
        fields = ('id','name', 'products')

p_s = ProductsSerializers(Product)
p_s.is_valid()
