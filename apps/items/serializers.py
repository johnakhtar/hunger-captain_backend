from .models import Item
from rest_framework import serializers
from apps.reviews.models import Review


class ItemSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(allow_null=True)

    class Meta:
        model = Item
        fields = '__all__'

    def like(self, obj):
        reviews = Review.objects.filter(item_id=obj.id)
        total_like= 0
        for review in reviews: 
            total_like += review.like_count
        return total_like