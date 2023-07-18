from django.shortcuts import render
from django.views.generic import View

from apps.pages.services.pages import PagesService


class HomePageView(View):
    template_name = "pages/home.html"
    service = PagesService()

    def get(self, request):
        """
        Get method to handle HTTP GET requests.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: The HTTP response object.
        """
        pages = self.service._get_all_pages()

        context = {
            "pages": pages,
        }

        return render(request, self.template_name, context)
