from asyncio.log import logger
import builtins
from cmath import log
from rest_framework.views import exception_handler
from django.http import JsonResponse
from .models import Errorcode
from rest_framework.decorators import api_view
from .serializers import ErrorcodeSerializer


def usererror(store_response):
    try:
        save_response = Errorcode.objects.create(message=str(store_response))
        save_response.save()
    except Exception as e:
        logger.error(e.__str__())


def get_response(message, status_code):
    return {
        "status_code": status_code,
        "error": message,
    }


class ExceptionMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        if response.status_code == 500:
            response = get_response(
                message="Internal server error, please try again later",
                status_code=response.status_code
            )
            logger.error(response)
            usererror(response)

            return JsonResponse(response, status=response['status_code'])

        if response.status_code == 404 and "Page not found" in str(response.content):
            response = get_response(
                message="Page not found, invalid url",
                status_code=response.status_code
            )
            logger.error(response)
            usererror(response)

            return JsonResponse(response, status=response['status_code'])

        if response.status_code == 404:
            response = get_response(
                message=logger.error(),
                status_code=response.status_code
            )
            logger.error(response)
            usererror(response)

            return JsonResponse(response, status=response['status_code'])

        if response.status_code == 505:
            response = get_response(
                message="HTTP version not support",
                status_code=response.status_code
            )
            logger.error(response)
            usererror(response)

            return JsonResponse(response, status=response['status_code'])

        return response
