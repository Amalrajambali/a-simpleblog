from django.urls import path
# from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView,CategoryView,CategoryListView,LikeView,AddCommentView

urlpatterns = [
    # path("",views.home, name="home")
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    # <int:pk> -oroninum oronn varan like article/1,ariticle/2 angane
    path('add_post/', AddPostView.as_view(), name="add_post"),  # pk=primarykey
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name="delete_post"),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/',CategoryListView, name='category-list'),
    path('like_post/<int:pk>',LikeView,name="like_post"),
    path('article/<int:pk>/add_comment/',AddCommentView.as_view(),name="add_comment"),
]
