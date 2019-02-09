from django.middleware.common import CommonMiddleware

from django.utils.deprecation import MiddlewareMixin

class CorsMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = '*'

        # 复杂POST请求，会先发送options请求，进行预检
        if request.method == 'OPTIONS':
            # Content-Type是客户端发磅的请求头。如果有多个请求头用逗号分隔
            response['Access-Control-Allow-Headers'] = 'Content-Type'
            response['Access-Control-Allow-Methods'] = 'PUT,DELETE'

        return response


