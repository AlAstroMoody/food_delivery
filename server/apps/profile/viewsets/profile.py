from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.main import IsUserProfile
from apps.profile.models import Profile
from apps.profile.serializers import ProfileSerializer


class ProfileViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsUserProfile,)
