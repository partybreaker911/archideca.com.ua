from apps.pages.models import Page


class PagesService:
    """
    Service class for Page model.

    Methods:
        _get_all_pages()
        _get_page_detail(page_id)
    """

    @staticmethod
    def _get_all_pages():
        """
        Retrieves all pages from the database that have associated tags.

        Returns:
            QuerySet: A queryset of Page objects with their associated tags.
        """
        return Page.objects.select_related("tags").filter(tags__isnull=False)

    @staticmethod
    def _get_page_detail(page_id):
        """
        Returns the details of a page with the given ID.

        Parameters:
            page_id (int): The ID of the page.

        Returns:
            Page: The page object with the specified ID, including its related tags.

        """
        return Page.objects.select_related("tags").filter(id=page_id).first()
