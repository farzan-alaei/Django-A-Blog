from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from .models import Post
# Create your views here.

def indexView(request):
    """
    a function based view to show index page
    """
    return render(request,"index.html")

class IndexView(TemplateView):
    """
    a class based view to show index page
    """
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex["name"] = "ali"
        contex["posts"] = Post.objects.all()
        return contex