from django.utils.deprecation import MiddlewareMixin

class RemoveNoIndexHeaderMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        # Only remove for sitemap and robots.txt
        if request.path in ["/sitemap.xml", "/robots.txt"]:
            response.headers.pop("X-Robots-Tag", None)
        return response
