from django.urls import path
from . import views

urlpatterns = [
    # 전체영와 정보 제공 (GET)
    path('movies/', views.movie_list),
    # 단일영화 정보 제공 (GET)
    path('movies/<int:movie_pk>/', views.movie_detail),
    # 리뷰 생성 (POST)
    path('movies/<int:movie_pk>/review/', views.review_create),
    # 리뷰정보 반환, 수정, 삭제 (GET, PUT, DELETE)
    path('review/<int:review_pk>/', views.review_detail),
    # 댓글 생성 (POST)
    path('review/<int:review_pk>/comment/', views.comment_create),
    # 댓글 정보 반환 (GET)
    path('comment/<int:comment_pk>/', views.comment_detail),
]
