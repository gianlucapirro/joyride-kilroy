from rest_framework import mixins, viewsets
from .models import Registrant
from .serializers import RegistrantSerializer

class RegistrantViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Registrant.objects.all()
    serializer_class = RegistrantSerializer
