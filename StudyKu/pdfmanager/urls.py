from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_pdf, name='upload_pdf'),
    path('', views.search_pdfs, name='search_pdfs'),
]


