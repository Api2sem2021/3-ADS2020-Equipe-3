from django.urls import include, path
from vagas import views

urlpatterns = [
    path('vagas/', include([
        path(
            '',
            views.VagaListView.as_view(),
            name='vaga_list'
        ),
        path(
            'novo/',
            views.VagaCreateView.as_view(),
            name='vaga_form'
        ),
        # path(
        #     'json/',
        #     views.autofill_campos_ocupacaoimovel,
        #     name='resposta_json'
        # ),
        path(
            '<int:pk>/',
            views.VagaUpdateView.as_view(),
            name='vaga_form'
        ),
    ])),
    path('competencias/', include([
        path(
            '',
            views.CompetenciaListView.as_view(),
            name='competencia_list'
        ),
        path(
            'novo/',
            views.CompetenciaCreateView.as_view(),
            name='competencia_form'
        ),
        path(
            '<int:pk>/',
            views.CompetenciaUpdateView.as_view(),
            name='competencia_form'
        ),
    ])),    
]