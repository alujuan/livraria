from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from livraria.models import Categoria
from livraria.models import Editora
from livraria.models import Autor
from livraria.models import Livro

from livraria.serializers import CategoriaSerializer
from livraria.serializers import EditoraSerializer
from livraria.serializers import AutorSerializer
from livraria.serializers import LivroSerializer
from livraria.serializers import LivroDetailSerializer
from livraria.serializers import LivroListSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer


class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return LivroListSerializer
        elif self.action == "retrieve":
            return LivroDetailSerializer
        return LivroSerializer

    serializer_classes = {
        "list": LivroListSerializer,
        "retrieve": LivroDetailSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, LivroSerializer)
