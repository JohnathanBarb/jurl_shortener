import random
import string
from rest_framework import serializers
from src.apps.url.models import Url

class CreateUrlSerializer(serializers.ModelSerializer):
    expires_at = serializers.DateTimeField(required=False)
    token = serializers.CharField(read_only=True)

    class Meta:
        model = Url
        fields = ["url", "expires_at", "token"]

    def __generate_token(self):
        return "".join(random.choices(string.ascii_letters + string.digits, k=5))

    def create(self, validated_data):
        # Generate a token until it's unique
        while True:
            token = self.__generate_token()
            if not Url.objects.filter(token=token).exists():
                break

        return Url.objects.create(token=token, **validated_data)
