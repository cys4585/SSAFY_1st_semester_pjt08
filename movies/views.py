from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Movie, Review, Comment
from .serializers import (
    MovieListSerializer, MovieSerializer,
    ReviewSerializer, CommentSerializer
)
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.db.models import Avg

# Create your views here.
@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(instance=movies, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(instance=movie)
    return Response(data=serializer.data)


@api_view(['POST'])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    # 리뷰정보 반환
    if request.method == 'GET':
        serializer = ReviewSerializer(instance=review)
        return Response(serializer.data)
    # 리뷰 수정
    elif request.method == 'PUT':
        serializer = ReviewSerializer(instance=review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    # 리뷰 삭제
    elif request.method == 'DELETE':
        review.delete()
        data = {
            'delete': f'{review_pk}번 review가 삭제되었습니다.',
        }
        return Response(data=data, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def comment_create(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    serializer = CommentSerializer(instance=comment)
    return Response(data=serializer.data)