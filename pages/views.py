from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def home_page_view(request):
    context = {
        "inventory_list": ["Widget 1", "Widget 2","Widget 3"], 
        "greeting": "Thank you for Visiting.",
    }
    return render(request, "home.html", context)

class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "123 Ur Mom's House"
        context["phone_number"] = "666-666-6666"
        return context
    
class ProductsPageView(TemplateView):
    template_name = "products.html"

    def get_context_data(self):
        context = {"product_list":["Phone","Tablet","Computer","Laptop"]}
        return context