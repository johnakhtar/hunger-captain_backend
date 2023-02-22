from rest_framework import generics
from .serializers import ReviewSerializer
from .models import Review

class ReviewList(generics.ListAPIView):
    queryset = Review.objects.order_by('-created_at').all()
    serializer_class = ReviewSerializer


class ReviewAdd(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


# Create your views here.
