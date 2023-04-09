from django.urls import path
from . import views
from django.views.generic.base import TemplateView, RedirectView

app_name = "blog"


urlpatterns = [
    path('fbv-index', views.indexView, name='fbv-index'),
    # path('cbv-index', TemplateView.as_view(template_name='index.html', extra_context={"name": "ali"}))
    path('cbv-index', views.IndexView.as_view(), name='cbv-index'),
    path(
        "go-to-index/",
        RedirectView.as_view(pattern_name="blog:cbv-index"),
        name="go-to-index",
    ),
]
