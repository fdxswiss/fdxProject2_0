# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from multiselectfield import MultiSelectField
import datetime

class Kontaktanfrage(models.Model):
    name = models.CharField(max_length=20, null=True)
    vorname = models.CharField(max_length=20, null=True)
    eMail = models.CharField(max_length=50, null=True)
    tel = models.CharField(max_length=20, null=True)
    beschreibung = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)

    def __str__(self):
        return self.name + " - " + self.vorname + " - " + str(self.updated)

class Firmeneintrag(models.Model):
    BRANCHEN = (
        ('Umzug', 'Umzug'),
        ('Reinigung', 'Reinigung'),
        ('Maler', 'Maler'),
        ('Architekt', 'Architekt'),
        ('Sanitär', 'Sanitär'),
        ('Schreiner', 'Schreiner'),
        ('Gartenbau', 'Gartenbau'),
        ('Elektriker', 'Elektriker'),
        ('Dachdecker', 'Dachdecker'),
        ('Bodenbeläge', 'Bodenbeläge'),
    )

    branche = MultiSelectField(choices=BRANCHEN)
    nameAnsprechperson = models.CharField(db_index=True, max_length=200, null=True)
    firmaName = models.CharField(db_index=True, max_length=200, null=True)
    plz = models.IntegerField(db_index=True)
    ort = models.CharField(db_index=True, max_length=200, null=True)
    tel = models.CharField(db_index=True, max_length=200, null=True)
    eMail = models.EmailField(db_index=True, max_length=200, null=True)
    beschreibung = models.TextField(null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)

    def __str__(self):
        return self.name + ' - ' + self.eMail + ' - ' + str(self.timestamp)


class UmzugForm(models.Model):

    von = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    nach = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    art1 = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    art2 = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    art3 = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    art4 = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    art5 = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    art6 = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    keller = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    garage = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    estrich = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    fname = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    lname = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    firm_name = models.TextField(db_index=True, null=True, blank=True)
    mailList = models.TextField(db_index=True, null=True, blank=True)
    datum = models.CharField(db_index=True, null=True, max_length=200, blank=True)
    tel = models.CharField(db_index=True, null=True, max_length=200, blank=True)
    email = models.EmailField(db_index=True, max_length=200, null=True, blank=True)
    beschreibung = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)

    def __str__(self):
        return 'ID: ' + str(self.id) + ' - ' + 'Name: ' + str(self.fname) +' '+ str(self.lname) +' - '+ 'Timestamp: ' + str(self.timestamp)

class ReinigungForm(models.Model):

    art1reinigung = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    art2reinigung = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    groesse = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    abgabegarantie = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    teppichreinigung = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    lamellenstoren = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    garage = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    estrich = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    keller = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    fname = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    lname = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    firm_name = models.TextField(db_index=True, null=True, blank=True)
    mailList = models.TextField(db_index=True, null=True, blank=True)
    datum = models.CharField(db_index=True, null=True, max_length=200, blank=True)
    tel = models.CharField(db_index=True, null=True, max_length=200, blank=True)
    email = models.EmailField(db_index=True, max_length=200, null=True, blank=True)
    beschreibung = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)

    def __str__(self):
        return str(self.id) + 'Name: ' + str(self.fname) +' '+ str(self.lname) +' '+ 'Timestamp: ' + str(self.timestamp)

class MalerForm(models.Model):

    art1maler = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    groesse = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    heizkoerper = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    fenserrahmen = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    tuerrahmen = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    gipserarbeiten = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    isolierarbeiten = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    stuckarbeiten = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    fname = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    lname = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    firm_name = models.TextField(db_index=True, null=True, blank=True)
    mailList = models.TextField(db_index=True, null=True, blank=True)
    datum = models.CharField(db_index=True, null=True, max_length=200, blank=True)
    tel = models.CharField(db_index=True, null=True, max_length=200, blank=True)
    email = models.EmailField(db_index=True, max_length=200, null=True, blank=True)
    beschreibung = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)

    def __str__(self):
        return 'Name: ' + str(self.fname) +' '+ str(self.lname) +' '+ 'Timestamp: ' + str(self.timestamp)

class SchreinerForm(models.Model):

    reparaturen = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    einbauschrank = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    regal = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    auftragsbeschreibung = models.TextField(db_index=True, max_length=500, null=True, blank=True)
    allgemein = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    fname = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    lname = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    firm_name = models.TextField(db_index=True, null=True, blank=True)
    mailList = models.TextField(db_index=True, null=True, blank=True)
    datum = models.CharField(db_index=True, null=True, max_length=200, blank=True)
    tel = models.CharField(db_index=True, null=True, max_length=200, blank=True)
    email = models.EmailField(db_index=True, max_length=200, null=True, blank=True)
    beschreibung = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)

    def __str__(self):
        return 'Name: ' + str(self.fname) +' '+ str(self.lname) +' '+ 'Timestamp: ' + str(self.timestamp)

class DachdeckerForm(models.Model):

    ziegeldach = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    kunststoffdach = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    flachdach = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    asphaltdach = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    regenrinnen = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    auftragsbeschreibung = models.TextField(db_index=True, max_length=500, null=True, blank=True)
    fname = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    lname = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    firm_name = models.TextField(db_index=True, null=True, blank=True)
    mailList = models.TextField(db_index=True, null=True, blank=True)
    datum = models.CharField(db_index=True, null=True, max_length=200, blank=True)
    tel = models.CharField(db_index=True, null=True, max_length=200, blank=True)
    email = models.EmailField(db_index=True, max_length=200, null=True, blank=True)
    beschreibung = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)

    def __str__(self):
        return 'Name: ' + str(self.fname) +' '+ str(self.lname) +' '+ 'Timestamp: ' + str(self.timestamp)

class ElektrikerForm(models.Model):

    sicherheitstechnik = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    schwachstromarbeiten = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    starkstromarbeiten = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    apparate = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    weitere = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    auftragsbeschreibung = models.TextField(db_index=True, max_length=500, null=True, blank=True)
    fname = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    lname = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    firm_name = models.TextField(db_index=True, null=True, blank=True)
    mailList = models.TextField(db_index=True, null=True, blank=True)
    datum = models.CharField(db_index=True, null=True, max_length=200, blank=True)
    tel = models.CharField(db_index=True, null=True, max_length=200, blank=True)
    email = models.EmailField(db_index=True, max_length=200, null=True, blank=True)
    beschreibung = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)

    def __str__(self):
        return 'Name: ' + str(self.fname) +' '+ str(self.lname) +' '+ 'Timestamp: ' + str(self.timestamp)

class ArchitektForm(models.Model):
    neubauprojekt = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    aufstockung = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    innenumbau = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    sanierung = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    weitere = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    auftragsbeschreibung = models.TextField(db_index=True, max_length=500, null=True, blank=True)
    fname = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    lname = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    firm_name = models.TextField(db_index=True, null=True, blank=True)
    mailList = models.TextField(db_index=True, null=True, blank=True)
    datum = models.CharField(db_index=True, null=True, max_length=200, blank=True)
    tel = models.CharField(db_index=True, null=True, max_length=200, blank=True)
    email = models.EmailField(db_index=True, max_length=200, null=True, blank=True)
    beschreibung = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)

    def __str__(self):
        return 'Name: ' + str(self.fname) +' '+ str(self.lname) +' '+ 'Timestamp: ' + str(self.timestamp)

class BodenbelaegeForm(models.Model):

    groesse = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    parkett = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    laminat = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    teppich = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    vinyl = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    weitere = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    auftragsbeschreibung = models.TextField(db_index=True, max_length=500, null=True, blank=True)
    fname = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    lname = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    firm_name = models.TextField(db_index=True, null=True, blank=True)
    mailList = models.TextField(db_index=True, null=True, blank=True)
    datum = models.CharField(db_index=True, null=True, max_length=200, blank=True)
    tel = models.CharField(db_index=True, null=True, max_length=200, blank=True)
    email = models.EmailField(db_index=True, max_length=200, null=True, blank=True)
    beschreibung = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)

    def __str__(self):
        return 'Name: ' + str(self.fname) +' '+ str(self.lname) +' '+ 'Timestamp: ' + str(self.timestamp)

class SanitaerForm(models.Model):

    anlagen = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    heizung = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    reparaturen = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    amaturen = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    allgemein = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    auftragsbeschreibung = models.TextField(db_index=True, max_length=500, null=True, blank=True)
    fname = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    lname = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    firm_name = models.TextField(db_index=True, null=True, max_length=200, blank=True)
    mailList = models.TextField(db_index=True, null=True, max_length=200, blank=True)
    datum = models.CharField(db_index=True, null=True, max_length=200, blank=True)
    tel = models.CharField(db_index=True, null=True, max_length=200, blank=True)
    email = models.EmailField(db_index=True, max_length=200, null=True, blank=True)
    beschreibung = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)

    def __str__(self):
        return 'Name: ' + str(self.fname) +' '+ str(self.lname) +' '+ 'Timestamp: ' + str(self.timestamp)

class GartenbauForm(models.Model):

    gartenpflege = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    gartensanierung = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    baumschnitt = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    zaun = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    allgemein = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    auftragsbeschreibung = models.TextField(db_index=True, max_length=500, null=True, blank=True)
    fname = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    lname = models.CharField(db_index=True, max_length=200, null=True, blank=True)
    firm_name = models.TextField(db_index=True, null=True, blank=True)
    mailList = models.TextField(db_index=True, null=True, blank=True)
    datum = models.CharField(db_index=True, null=True, max_length=200, blank=True)
    tel = models.CharField(db_index=True, null=True, max_length=200, blank=True)
    email = models.EmailField(db_index=True, max_length=200, null=True, blank=True)
    beschreibung = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)

    def __str__(self):
        return 'Name: ' + str(self.fname) +' '+ str(self.lname) +' '+ 'Timestamp: ' + str(self.timestamp)
