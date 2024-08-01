import json
import uuid
from datetime import datetime

from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin


class CustomErrorHandlerMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        response_data = {"error": "Internal Server Error", "message": str(exception)}
        return JsonResponse(response_data, status=500)


class CustomResponseMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if response["Content-Type"] == "application/json":
            try:
                response_data = json.loads(response.content)
            except json.JSONDecodeError:
                response_data = {}

            custom_response = {
                "version": "1.0.0",
                "process_id": str(uuid.uuid4()),
                "timestamp": str(datetime.now()),
                "data": response_data,
            }

            response.content = json.dumps(custom_response)
            response["Content-Length"] = len(response.content)

        return response
