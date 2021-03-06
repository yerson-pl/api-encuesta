from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import EncuestaSerializer, PreguntaSerializer, OpcionPreguntaSerializer, ResultadoSerializer, UserSerializer
from ..models import Encuesta, Pregunta, OpcionPregunta, Resultado
from apps.encuestas.api.permissions import IsOwnerOrReadOnly


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class EncuestaList(generics.ListCreateAPIView):
    queryset = Encuesta.objects.all()
    serializer_class = EncuestaSerializer
    name = 'encuesta-list'


class EncuestaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Encuesta.objects.all()
    serializer_class = EncuestaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)
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


class LoginView(APIView):
    permission_classes = ()

    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)
