from rest_framework import serializers
from rest_framework.authtoken.models import Token
from ..models import Encuesta, Pregunta, OpcionPregunta, Resultado
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user


class ResultadoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Resultado
        fields = '__all__'


class OpcionPreguntaSerializer(serializers.ModelSerializer):
    resultados = ResultadoSerializer(many=True, required=False)

    class Meta:
        model = OpcionPregunta
        fields = '__all__'


class PreguntaSerializer(serializers.ModelSerializer):
    opciones = OpcionPreguntaSerializer(many=True, required=False)

    class Meta:
        model = Pregunta
        fields = '__all__'


class EncuestaSerializer(serializers.ModelSerializer):
    preguntas = PreguntaSerializer(many=True, required=False)

    class Meta:
        model = Encuesta
        fields = '__all__'




