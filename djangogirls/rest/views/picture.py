from core.models import Picture
from rest.serializers import PictureSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from django_filters.rest_framework import DjangoFilterBackend


class PictureView(mixins.CreateModelMixin,
                                          mixins.RetrieveModelMixin,
                                          mixins.DestroyModelMixin,
                                          mixins.ListModelMixin,
                                          GenericViewSet):

    serializer_class = PictureSerializer

    #def perform_create(self, serializer):


    filter_fields = ('created_at', 'category')
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        return Picture.objects.all()





