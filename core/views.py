from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


@api_view(["GET"])
def my_func(request):
    context={
        "message":"Hello World!"
    }
    return Response(context,status=status.HTTP_200_OK)