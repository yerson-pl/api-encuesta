from django.conf.urls import url 
from apps.encuestas.api import views 
 
 
urlpatterns = [
    url(r'^login/$',  
        views.LoginView.as_view(),  
        name="login"),
    url(r'^users/$',  
        views.UserCreate.as_view(),  
        name="user_create"),
    url(r'^encuestas/$',  
        views.EncuestaList.as_view(),  
        name=views.EncuestaList.name), 
    url(r'^encuestas/(?P<pk>[0-9]+)$',  
        views.EncuestaDetail.as_view(), 
        name=views.EncuestaDetail.name), 
    url(r'^encuestas/(?P<pk>[0-9]+)/preguntas/',  
        views.PreguntaList.as_view(), 
        name=views.PreguntaList.name), 
    url(r'^opcion-preguntas/$',  
        views.OpcionPreguntaList.as_view(),  
        name=views.OpcionPreguntaList.name),
    url(r'^resultados/$',  
        views.ResultadoList.as_view(),  
        name=views.ResultadoList.name), 
    ]