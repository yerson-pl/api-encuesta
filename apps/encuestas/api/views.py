from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from .serializers import EncuestaSerializer, PreguntaSerializer, OpcionPreguntaSerializer, ResultadoSerializer, UserSerializer
from ..models import Encuesta, Pregunta, OpcionPregunta, Resultado


class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer
    

class EncuestaList(generics.ListCreateAPIView):
    queryset = Encuesta.objects.all()
    serializer_class = EncuestaSerializer
    name = 'encuesta-list'


class EncuestaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Encuesta.objects.all()
    serializer_class = EncuestaSerializer
    name = 'encuesta-detail'


class PreguntaList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Pregunta.objects.filter(encuesta_id=self.kwargs["pk"])
        return queryset
    serializer_class = PreguntaSerializer
    name = 'pregunta-list'


class PreguntaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer
    name = 'pregunta-detail'


class OpcionPreguntaList(generics.ListCreateAPIView):
    queryset = OpcionPregunta.objects.all()
    serializer_class = OpcionPreguntaSerializer
    name = 'opcion-list'


class ResultadoList(generics.CreateAPIView):
    serializer_class = ResultadoSerializer
    name = 'resultado-list'