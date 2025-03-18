import random
import string
from rest_framework import serializers
from src.apps.url.models import Url

class CreateUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ["url", "expires_at"]
        extra_kwargs = {
            "expires_at": {"required": False}
        }

    def __generate_token(self):
        return "".join(random.choices(string.ascii_letters + string.digits, k=5))

    def create(self, validated_data):
        # Generate a token until it's unique
        while True:
            token = self.__generate_token()
            if not Url.objects.filter(token=token).exists():
                break

        return Url.objects.create(token=token, **validated_data)

# {"url": "https://www.google.com", "expires_at": "2025-03-18T10:00:00Z"}
