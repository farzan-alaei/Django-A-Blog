from django.urls import path
from . import views
from django.views.generic.base import TemplateView, RedirectView

app_name = "blog"


urlpatterns = [
    path('cbv-index', views.IndexView.as_view(), name='cbv-index'),
    path('post/', views.PostListView.as_view(), name="post_list"),
    path(
        "go-to-google/<int:pk>",
        views.RedirectToGoogle.as_view(),
        name="go-to-google",
    ),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name="post-detail")
]
