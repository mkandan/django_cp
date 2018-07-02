from django.urls import path
from . import views


urlpatterns=[
    path('', views.index, name='index'),
    #if someone goes to empty path, go into views
    #file and runs index function.
    #later on, can reference this by the index html file
    path('specifics/<int:question_id>/', views.detail, name='detail'),
    #if there's no additional part to URL then show detail view
    #adding specifics lets us change the 
    path('<int:question_id>/results/', views.results, name='results'),
    #if there is results at end of url, then display results view
    path('<int:question_id>/vote/', views.vote, name='vote'),
    #if there is a vote at end of url, then display vote view
]
