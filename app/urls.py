from django.urls import path
from .views import *
urlpatterns = [
    path("", index, name="home"),
    path("etudiants/", etudiant, name="etudiants"),
    path("etudiants/add", etudiant_add, name="add_etudiants"),
    path("etudiants/etudiant_delete/<id>", etudiant_delete, name="delete_etudiant"),
    path("etudiants/etudiant_edit/<id>", etudiant_edit, name="update_etudiant"),
    path("etudiants/etudiant_noter/<id>", etudaint_noter, name="noter_etudiant"),
    path("etudiants/etudiant_notes/<id>", etudiant_notes, name="notes_etudiant"),
    path("notes/", notes, name="notes"),
    path("notes/noter", noter, name="noter"),
]
