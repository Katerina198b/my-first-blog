from rest_framework import serializers

from core.models import Picture


class PictureSerializer(serializers.ModelSerializer):
    cat = serializers.ReadOnlyField(source='category')

    class Meta:
        model = Picture
        fields = ('file', 'cat',  'created_at', 'category')


