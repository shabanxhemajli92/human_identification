from django.urls import path,include
from .views import create_human,view_humans

urlpatterns = [
    #path('identification/', include('identification.urls', namespace='identification')),
    path('create/', create_human, name='create_human'),
    path('humans/', view_humans, name='view_humans'),
]