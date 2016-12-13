from rest_framework import mixins, permissions, viewsets

from adhocracy4.api.permissions import IsModerator

from .models import Document
from .serializers import DocumentSerializer


class DocumentViewSet(mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = (
        permissions.IsAuthenticated, IsModerator,
    )
