from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Etudiant(models.Model):
    Nom = models.CharField('Nom de l\'étudiant', max_length=50)
    prenom = models.CharField("Prénom de l\'étudiant", max_length=50)
    salle_de_classe = models.CharField( max_length=10)

    SEXE_CHOICE = [
        ('Masculin', 'Masculin'),
        ('Féminin','Féminin')
    ]
    sexe = models.CharField( max_length=50, choices = SEXE_CHOICE)
    numero_de_telephone = models.PositiveIntegerField()
    

    def get_notes(self):
        return  Notation.objects.filter(etudiant = self)

    def __str__(self):
        return self.Nom + " " + self.prenom

    def get_tautaux(self):
        notes = Notation.objects.filter(etudiant = self)
        somme = 0
        for item in notes:
            somme = somme + item.get_total()
        return somme
class Critere(models.Model):

    nom = models.CharField( max_length=50)
    note_maximale = models.PositiveIntegerField()

    class Meta:
        verbose_name = ("Critere")
        verbose_name_plural = ("Criteres")

    def __str__(self):
        return self.nom

class note(models.Model):

    etudiant = models.ForeignKey("Etudiant" ,on_delete=models.CASCADE)
    Critere = models.ForeignKey("Critere" ,on_delete=models.CASCADE)
    note = models.PositiveIntegerField()
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        # return f"Note de l'étudiant {self.etudiant} dans le critère '{self.Critere}"
        return f'{self.note}'


class Notation(models.Model):
    etudiant = models.ForeignKey("Etudiant",  on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    tenue_conforme = models.PositiveIntegerField()
    demarche_posture = models.PositiveIntegerField('Démarche / posture')   
    eloquence = models.PositiveIntegerField("Eloquence")
    Honnetete = models.PositiveIntegerField("Honeteté")
    cas_pratique = models.PositiveIntegerField()
    remarque = models.TextField(blank=True, null=True)


    def get_total(self):

        return self.tenue_conforme + self.demarche_posture + self.eloquence + self.Honnetete + self.cas_pratique

   

   

