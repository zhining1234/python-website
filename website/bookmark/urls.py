from django.urls import path
# from bookmark.views import BookmarkLV, BookmarkDV
from bookmark import views


app_name = 'bookmark'
urlpatterns = [
    # 리스트: http://127.0.0.1:8000/bookmark/
    path('', views.BookmarkLV.as_view(), name='index'),

    # 상세페이지: http://127.0.0.1:8000/bookmark/1/
    path('<int:pk>/', views.BookmarkDV.as_view(), name='detail'),

    # 생성: http://127.0.0.1:8000/bookmark/add/
    path('add/', views.BookmarkCreateView.as_view(), name="add",),

    # 수정: http://127.0.0.1:8000/bookmark/1/update/
    path('<int:pk>/update/', views.BookmarkUpdateView.as_view(), name="update",),

    # 삭제: http://127.0.0.1:8000/bookmark/1/delete/
    path('<int:pk>/delete/', views.BookmarkDeleteView.as_view(), name="delete",),
]

