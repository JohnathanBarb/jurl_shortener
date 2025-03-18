from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from src.apps.url.models import Url
from src.apps.url.serializers import CreateUrlSerializer


class CreateUrlView(APIView):
    serializer_class = CreateUrlSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_shortened_url(request, token):
    url_object = Url.objects.get(token=token)
    # TODO: redirect to the original url

    return Response(
        {
            "url": url_object.url,
        },
        status=status.HTTP_200_OK,
    )
