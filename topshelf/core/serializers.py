from rest_framework import serializers

from core.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Profile
        fields = ('__all__')