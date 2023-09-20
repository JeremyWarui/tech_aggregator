from typing import Any

# Create your views here.
from django.views.generic import ListView
from .models import Episode

class HomePageView(ListView):
    """class to render homepage"""
    template_name = "homepage.html"
    model = Episode

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["episodes"] = Episode.objects.filter().order_by(
            "-pub_date")[:10]
        return context
