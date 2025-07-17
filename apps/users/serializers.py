from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.first_name
        token['first_name'] = user.first_name
        token['last_name'] = user.first_name
        token['profile_image'] = user.profile_image.url

        return token
