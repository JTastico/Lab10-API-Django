from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('serie', views.SeriesView.as_view(), name='series'),
    path('serie/<int:serie_id>', views.SerieDetailView.as_view()),
    path('categoria/', views.CategoriaListCreateView.as_view(), name='categoria-list-create'),
    path('categoria/<int:pk>/', views.CategoriaDetailView.as_view(), name='categoria-detail'),
    path('producto/', views.ProductoListCreateView.as_view(), name='producto-list-create'),
    path('producto/<int:pk>/', views.ProductoDetailView.as_view(), name='producto-detail'),
]
