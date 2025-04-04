from rest_framework import generics
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticated


class ReviewCreateListView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
