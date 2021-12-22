from django.urls import path

from blog.views import BlogCreateView, BlogDeleteView, BlogDetailsView, BlogListView, BlogUpdateView

app_name="blog"

urlpatterns = [
    path('', BlogListView.as_view(), name="home"), 
    path('create/', BlogCreateView.as_view(), name='create'),
    path('<int:pk>',BlogDetailsView.as_view(),name="detail"),
    path('<int:pk>/update/', BlogUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', BlogDeleteView.as_view(),name='delete')
]