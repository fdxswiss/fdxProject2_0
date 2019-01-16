from django.db import models
from multiselectfield import MultiSelectField

class Firma(models.Model):

    BRANCHEN = (
        ('Umzug', 'Umzug'),
        ('Reinigung', 'Reinigung'),
        ('Maler', 'Maler'),
        ('Architekt', 'Architekt'),
        ('Sanitaer', 'Sanitaer'),
        ('Schreiner', 'Schreiner'),
        ('Gartenbau', 'Gartenbau'),
        ('Elektriker', 'Elektriker'),
        ('Dachdecker', 'Dachdecker'),
        ('Bodenbelaege', 'Bodenbelaege'),
    )

    branche = MultiSelectField(choices=BRANCHEN, null=True)
    name = models.CharField(db_index=True, max_length=200, null=True)
    plz = models.CharField(db_index=True, max_length=5, null=True)
    ort = models.CharField(db_index=True, max_length=200, null=True)
    strasse = models.CharField(max_length=200, null=True)
    nr = models.CharField(max_length=200, null=True)
    beschreibung = models.TextField()
    eMail = models.EmailField(db_index=True, max_length=200, null=True)
    homepage = models.CharField(db_index=True, max_length=200, null=True)
    firm_logo = models.ImageField(db_index=True, upload_to='treasure_image')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)

    def __str__(self):
        return self.name + " in " + self.plz + " Branchen: " + str(self.branche)
