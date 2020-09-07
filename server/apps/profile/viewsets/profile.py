from rest_framework.viewsets import ModelViewSet

from apps.profile.models import Profile
from apps.profile.serializers import ProfileSerializer


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
