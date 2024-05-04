from rest_framework import serializers

from .models import Media

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = "__all__"

    # def get_file(self, obj):
    #     return obj.file.url
