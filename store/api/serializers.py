from rest_framework import serializers

from store.models import Product


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id',
            "title",
            "description",
            "owner",
            "cost",
            "price",
            "image",
        )

    def get_owner(self, obj):
        return obj.user.username
