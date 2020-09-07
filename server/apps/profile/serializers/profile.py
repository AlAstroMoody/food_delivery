from rest_framework.serializers import ModelSerializer

from apps.profile.models import Profile


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'name', 'user', 'birthday',
                  'address', 'phone', 'email')
