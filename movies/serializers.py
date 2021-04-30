from rest_framework import serializers
from .models import Movie, Review, Comment



class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review', )


class ReviewSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = (
            'id', 'title', 'content', 
            'rank', 'movie', 'comment_set',
        )
        read_only_fields = ('movie', )


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'



class MovieSerializer(serializers.ModelSerializer):
    review_set = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = (
            'id', 'title', 'overview', 'release_date',
            'poster_path', 'review_set',
        )