from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from .models import Post
from django.shortcuts import redirect, get_object_or_404

# Create your views here.

# Function Base view show a template
'''
def indexView(request):
    """
    a function based view to show index page
    """
    return render(request,"index.html")
'''

class IndexView(TemplateView):
    """
    a class based view to show index page
    """
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ali"
        context["posts"] = Post.objects.all()
        return context
    



''' FBV for redirect
def redirectToGoogle(request):
    return redirect("https://google.com")
'''

class RedirectToGoogle(RedirectView):
    url = "https://google.com"

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args, **kwargs)