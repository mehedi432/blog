from django.views.generic import TemplateView


class BlogHomeView(TemplateView):
    template_name = "blog/home.html"


