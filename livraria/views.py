from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from livraria.models import Categoria
from livraria.models import Editora
from livraria.models import Livro

from livraria.serializers import CategoriaSerializer
from livraria.serializers import EditoraSerializer
from livraria.serializers import LivroSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer