from django.utils.deprecation import MiddlewareMixin

class CORS(MiddlewareMixin):
    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = "*"
        response['Access-Control-Allow-Headers'] = "Content-Type"
        response['Access-Control-Allow-Method'] = "PUT,DELETE"
        return response