from django.urls import path, include
from .models import Snakers
from rest_framework import routers, serializers, viewsets, mixins

class SnakersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Snakers
        fields = ['model_name', 'color', 'price', 'brand', 'category']

class SnakersViewSetMixin(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):

    queryset = Snakers.objects.all()
    serializer_class = SnakersSerializer
    

class SnakersViewSet(viewsets.ModelViewSet):
    queryset = Snakers.objects.all()
    serializer_class = SnakersSerializer

router = routers.DefaultRouter()
router.register(r'snakers', SnakersViewSet)
router.register(r'snakers-mixin', SnakersViewSetMixin)

urlpatterns = [
    path('', include(router.urls)),
]