from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView, RedirectView

app_name = "blog"


urlpatterns = [
    # path('cbv-index', views.IndexView.as_view(), name='cbv-index'),
    # path('post/', views.PostListView.as_view(), name="post_list"),
    path(
        "go-to-google/<int:pk>",
        views.RedirectToGoogle.as_view(),
        name="go-to-google",
    ),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name="post-detail"),
    path('post/create/', views.PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/edit/', views.PostEditView.as_view(),name='post-edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('api/v1/', include('blog.api.v1.urls'))

]
