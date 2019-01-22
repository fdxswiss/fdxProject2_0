#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from fdx_mail.models import UmzugForm, ReinigungForm, MalerForm, ArchitektForm, BodenbelaegeForm, DachdeckerForm, ElektrikerForm, GartenbauForm, SchreinerForm, SanitaerForm
from fdx_mail.models import Firmeneintrag, Kontaktanfrage

class Kontaktformular(forms.ModelForm):
    class Meta:
        model = Kontaktanfrage
        fields = ['name','vorname', 'eMail', 'tel', 'beschreibung']
        labels = {
            'name':'',
            'vorname':'',
            'eMail':'',
            'tel':'',
            'beschreibung':'',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name', 'style': 'margin-top: 20px'}),
            'vorname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vorname', 'style': 'margin-top: 20px'}),
            'eMail': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-Mail Adresse', 'style': 'margin-top: 20px'}),
            'tel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobiltelefon', 'style': 'margin-top: 20px'}),
            'beschreibung': forms.Textarea(attrs={'class': 'form-control', 'style': 'height:150px; margin-top:20px', 'placeholder': 'Ihre Anmerkung'}),
        }

class EintragFormular(forms.ModelForm):
    class Meta:
        model = Firmeneintrag
        fields = ['firma', 'name', 'plz', 'ort', 'eMail', 'beschreibung', 'branche']
        labels = {
            'firma':'',
            'name':'',
            'plz':'',
            'ort':'',
            'eMail':'',
            'beschreibung':'',
            'branche':'Wählen Sie Ihre Branche/n',
        }
        widgets = {
            'firma': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Firma', 'style': 'margin-top: 20px'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ansprechperson', 'style': 'margin-top: 20px'}),
            'plz': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Postleitzahl', 'style': 'margin-top: 20px'}),
            'ort': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ort', 'style': 'margin-top: 20px'}),
            'strasse': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Strasse', 'style': 'margin-top: 20px'}),
            'nr': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nr.', 'style': 'margin-top: 20px'}),
            'eMail': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-Mail', 'style': 'margin-top: 20px'}),
            'beschreibung': forms.Textarea(attrs={'class': 'form-control', 'style': 'height:150px; margin-top:20px; margin-bottom:30px', 'placeholder': 'Firmen Beschreibung...'}),
            'branche': forms.CheckboxSelectMultiple(attrs={'class': 'multiCheckBox'}),
        }

class UmzugFormular(forms.ModelForm):
    class Meta:
        model = UmzugForm
        fields = {'fname','lname','von','nach','art1','art2','art3','art4',
                    'art5','art6','keller','garage','estrich','firm_name',
                    'mailList','datum','tel','email','beschreibung'}

        labels = {
            'fname':'',
            'lname':'',
            'von':'',
            'nach':'',
            'art1':'',
            'art2':'',
            'art3':'',
            'art4':'',
            'art5':'',
            'art6':'',
            'keller':'',
            'estrich':'',
            'garage':'',
            'firm_name':'',
            'mailList':'',
            'datum':'',
            'tel':'',
            'email':'',
            'beschreibung':'',
        }

        widgets = {
            'von': forms.TextInput(attrs={'id':'von' , 'placeholder':'Postleitzahl/Ort', 'style':'width:70%', 'required':'False'}),
            'nach': forms.TextInput(attrs={'id':'nach' , 'placeholder':'Postleitzahl/Ort', 'style':'width:70%', 'required':'False'}),
            'art1': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False'}),
            'art2': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False'}),
            'art3': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False'}),
            'art4': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False'}),
            'art5': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False'}),
            'art6': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False'}),
            'keller': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False'}),
            'estrich': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False'}),
            'garage': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False'}),

            'mailList': forms.Textarea(attrs={'id':'mailList', 'style':'height:150px; margin-top:20px; display:none;', 'required':'False'}),
            'firm_name': forms.Textarea(attrs={'id':'id_send', 'style': 'height:150px; margin-top:20px', 'placeholder': 'Anfragen werden an Unternehmen in der Liste weitergeleitet.', 'required':'False', 'readonly':'True'}),
            'datum': forms.TextInput(attrs={'type':'date', 'id':'date' , 'style':'margin-top: 20px', 'required':'False'}),
            'fname': forms.TextInput(attrs={'required':'False', 'placeholder':'Vorname'}),
            'lname': forms.TextInput(attrs={'required':'False', 'placeholder':'Nachname'}),
            'tel': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':'Mobil-Nummer'}),
            'email': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':'Email Adresse'}),
            'beschreibung': forms.Textarea(attrs={'style':'height:150px; margin-top:20px;', 'required':'False', 'placeholder':'zustzliche Angaben'}),
        }

class ReinigungFormular(forms.ModelForm):
    class Meta:
        model = ReinigungForm
        fields = {'art1reinigung','art2reinigung','groesse','abgabegarantie','teppichreinigung','lamellenstoren','garage','estrich','keller','fname','lname', 'firm_name','mailList','datum','tel','email','beschreibung'}
        labels = {
                    'art1reinigung':'',
                    'art2reinigung':'',
                    'groesse':'',
                    'abgabegarantie':'',
                    'teppichreinigung':'',
                    'lamellenstoren':'',
                    'garage':'',
                    'estrich':'',
                    'keller':'',
                    'fname':'',
                    'lname':'',
                    'firm_name':'',
                    'mailList':'',
                    'datum':'',
                    'tel':'',
                    'email':'',
                    'beschreibung':'',
                }

        widgets = {
                    'art1reinigung': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'art2reinigung': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'groesse':  forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':'Fläche in m2'}),
                    'abgabegarantie':  forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'teppichreinigung': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'lamellenstoren': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'garage': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'estrich': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'keller': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'mailList': forms.Textarea(attrs={'id':'mailList', 'style':'height:150px; margin-top:20px; display:none;', 'required':'False'}),
                    'firm_name': forms.Textarea(attrs={'id':'id_send', 'style': 'height:150px; margin-top:20px', 'placeholder': 'Anfragen werden an Unternehmen in der Liste weitergeleitet.', 'required':'False', 'readonly':'True'}),
                    'datum': forms.TextInput(attrs={'type':'date', 'id':'date' , 'style':'margin-top: 20px', 'required':'False'}),
                    'fname': forms.TextInput(attrs={'required':'False', 'placeholder':'Vorname'}),
                    'lname': forms.TextInput(attrs={'required':'False', 'placeholder':'Nachname'}),
                    'tel': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':'Mobil-Nummer'}),
                    'email': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':'Email Adresse'}),
                    'beschreibung': forms.Textarea(attrs={'style':'height:150px; margin-top:20px;', 'required':'False', 'placeholder':'zustzliche Angaben'}),
                }

class MalerFormular(forms.ModelForm):
    class Meta:
        model = MalerForm
        fields = {'art1maler','groesse','heizkoerper','fenserrahmen','tuerrahmen','gipserarbeiten','isolierarbeiten','stuckarbeiten','fname','lname', 'firm_name','mailList','datum','tel','email','beschreibung'}
        labels = {
                    'art1maler':'',
                    'groesse':'',
                    'heizkoerper':'',
                    'fenserrahmen':'',
                    'tuerrahmen':'',
                    'gipserarbeiten':'',
                    'isolierarbeiten':'',
                    'stuckarbeiten':'',
                    'fname':'',
                    'lname':'',
                    'firm_name':'',
                    'mailList':'',
                    'datum':'',
                    'tel':'',
                    'email':'',
                    'beschreibung':'',
                }
        widgets = {
                    'art1maler': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False'}),
                    'groesse': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'heizkoerper': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'fenserrahmen': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'tuerrahmen': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'gipserarbeiten': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'isolierarbeiten': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'stuckarbeiten': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'mailList': forms.Textarea(attrs={'id':'mailList', 'style':'height:150px; margin-top:20px; display:none;', 'required':'False'}),
                    'firm_name': forms.Textarea(attrs={'id':'id_send', 'style': 'height:150px; margin-top:20px', 'placeholder': 'Anfragen werden an Unternehmen in der Liste weitergeleitet.', 'required':'False', 'readonly':'True'}),
                    'datum': forms.TextInput(attrs={'type':'date', 'id':'date' , 'style':'margin-top: 20px', 'required':'False'}),
                    'fname': forms.TextInput(attrs={'required':'False', 'placeholder':'Vorname'}),
                    'lname': forms.TextInput(attrs={'required':'False', 'placeholder':'Nachname'}),
                    'tel': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':'Mobil-Nummer'}),
                    'email': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':'Email Adresse'}),
                    'beschreibung': forms.Textarea(attrs={'style':'height:150px; margin-top:20px;', 'required':'False', 'placeholder':'zustzliche Angaben'}),
                }

class SchreinerFormular(forms.ModelForm):
    class Meta:
        model = SchreinerForm
        fields = {'reparaturen','einbauschrank','regal','auftragsbeschreibung','allgemein','fname','lname', 'firm_name','mailList','datum','tel','email','beschreibung'}
        labels = {
                    'reparaturen':'',
                    'einbauschrank':'',
                    'regal':'',
                    'auftragsbeschreibung':'',
                    'allgemein':'',
                    'fname':'',
                    'lname':'',
                    'firm_name':'',
                    'mailList':'',
                    'datum':'',
                    'tel':'',
                    'email':'',
                    'beschreibung':'',
                }
        widgets = {
                    'reparaturen': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'einbauschrank': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'regal': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'auftragsbeschreibung': forms.Textarea(attrs={'style':'height:150px; margin-top:20px;', 'required':'False', 'placeholder':'Bschreiben Sie Ihren Auftrag.'}),
                    'allgemein': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'mailList': forms.Textarea(attrs={'id':'mailList', 'style':'height:150px; margin-top:20px; display:none;', 'required':'False'}),
                    'firm_name': forms.Textarea(attrs={'id':'id_send', 'style': 'height:150px; margin-top:20px', 'placeholder': 'Anfragen werden an Unternehmen in der Liste weitergeleitet.', 'required':'False', 'readonly':'True'}),
                    'datum': forms.TextInput(attrs={'type':'date', 'id':'date' , 'style':'margin-top: 20px', 'required':'False'}),
                    'fname': forms.TextInput(attrs={'required':'False', 'placeholder':'Vorname'}),
                    'lname': forms.TextInput(attrs={'required':'False', 'placeholder':'Nachname'}),
                    'tel': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':'Mobil-Nummer'}),
                    'email': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':'Email Adresse'}),
                    'beschreibung': forms.Textarea(attrs={'style':'height:150px; margin-top:20px;', 'required':'False', 'placeholder':'zustzliche Angaben'}),
                }

class DachdeckerFormular(forms.ModelForm):
    class Meta:
        model = DachdeckerForm
        fields = {'ziegeldach','kunststoffdach','flachdach','asphaltdach','regenrinnen','auftragsbeschreibung','fname','lname', 'firm_name','mailList','datum','tel','email','beschreibung'}
        labels = {
                    'ziegeldach':'',
                    'kunststoffdach':'',
                    'flachdach':'',
                    'asphaltdach':'',
                    'regenrinnen':'',
                    'auftragsbeschreibung':'',
                    'fname':'',
                    'lname':'',
                    'firm_name':'',
                    'mailList':'',
                    'datum':'',
                    'tel':'',
                    'email':'',
                    'beschreibung':'',
                }
        widgets = {
                    'ziegeldach': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'kunststoffdach': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'flachdach': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'asphaltdach': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'regenrinnen': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'auftragsbeschreibung': forms.Textarea(attrs={'style':'height:150px; margin-top:20px;', 'required':'False', 'placeholder':'Bschreiben Sie Ihren Auftrag.'}),
                    'mailList': forms.Textarea(attrs={'id':'mailList', 'style':'height:150px; margin-top:20px; display:none;', 'required':'False'}),
                    'firm_name': forms.Textarea(attrs={'id':'id_send', 'style': 'height:150px; margin-top:20px', 'placeholder': 'Anfragen werden an Unternehmen in der Liste weitergeleitet.', 'required':'False', 'readonly':'True'}),
                    'datum': forms.TextInput(attrs={'type':'date', 'id':'date' , 'style':'margin-top: 20px', 'required':'False'}),
                    'fname': forms.TextInput(attrs={'required':'False', 'placeholder':'Vorname'}),
                    'lname': forms.TextInput(attrs={'required':'False', 'placeholder':'Nachname'}),
                    'tel': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':'Mobil-Nummer'}),
                    'email': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':'Email Adresse'}),
                    'beschreibung': forms.Textarea(attrs={'style':'height:150px; margin-top:20px;', 'required':'False', 'placeholder':'zustzliche Angaben'}),
                }

class ElektrikerFormular(forms.ModelForm):
    class Meta:
        model = ElektrikerForm
        fields = {'sicherheitstechnik','schwachstromarbeiten','starkstromarbeiten','apparate','weitere','auftragsbeschreibung','fname','lname', 'firm_name','mailList','datum','tel','email','beschreibung'}
        labels = {
                    'sicherheitstechnik':'',
                    'schwachstromarbeiten':'',
                    'starkstromarbeiten':'',
                    'apparate':'',
                    'weitere':'',
                    'auftragsbeschreibung':'',
                    'fname':'',
                    'lname':'',
                    'firm_name':'',
                    'mailList':'',
                    'datum':'',
                    'tel':'',
                    'email':'',
                    'beschreibung':'',
                }
        widgets = {
                    'sicherheitstechnik': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'schwachstromarbeiten': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'starkstromarbeiten': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'apparate': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'weitere': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'auftragsbeschreibung': forms.Textarea(attrs={'style':'height:150px; margin-top:20px;', 'required':'False', 'placeholder':'Bschreiben Sie Ihren Auftrag.'}),
                    'mailList': forms.Textarea(attrs={'id':'mailList', 'style':'height:150px; margin-top:20px; display:none;', 'required':'False'}),
                    'firm_name': forms.Textarea(attrs={'id':'id_send', 'style': 'height:150px; margin-top:20px', 'placeholder': 'Anfragen werden an Unternehmen in der Liste weitergeleitet.', 'required':'False', 'readonly':'True'}),
                    'datum': forms.TextInput(attrs={'type':'date', 'id':'date' , 'style':'margin-top: 20px', 'required':'False'}),
                    'fname': forms.TextInput(attrs={'required':'False', 'placeholder':'Vorname'}),
                    'lname': forms.TextInput(attrs={'required':'False', 'placeholder':'Nachname'}),
                    'tel': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':'Mobil-Nummer'}),
                    'email': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':'Email Adresse'}),
                    'beschreibung': forms.Textarea(attrs={'style':'height:150px; margin-top:20px;', 'required':'False', 'placeholder':'zustzliche Angaben'}),
                }

class GartenbauFormular(forms.ModelForm):
    class Meta:
        model = GartenbauForm
        fields = {'gartenpflege','gartensanierung','baumschnitt','zaun','allgemein','auftragsbeschreibung','fname','lname', 'firm_name','mailList','datum','tel','email','beschreibung'}
        labels = {
                    'gartenpflege':'',
                    'gartensanierung':'',
                    'baumschnitt':'',
                    'zaun':'',
                    'allgemein':'',
                    'auftragsbeschreibung':'',
                    'fname':'',
                    'lname':'',
                    'firm_name':'',
                    'mailList':'',
                    'datum':'',
                    'tel':'',
                    'email':'',
                    'beschreibung':'',
                }
        widgets = {
                    'gartenpflege': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'gartensanierung': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'baumschnitt': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'zaun': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'allgemein': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'auftragsbeschreibung': forms.Textarea(attrs={'style':'height:150px; margin-top:20px;', 'required':'False', 'placeholder':'Bschreiben Sie Ihren Auftrag.'}),
                    'mailList': forms.Textarea(attrs={'id':'mailList', 'style':'height:150px; margin-top:20px; display:none;', 'required':'False'}),
                    'firm_name': forms.Textarea(attrs={'id':'id_send', 'style': 'height:150px; margin-top:20px', 'placeholder': 'Anfragen werden an Unternehmen in der Liste weitergeleitet.', 'required':'False', 'readonly':'True'}),
                    'datum': forms.TextInput(attrs={'type':'date', 'id':'date' , 'style':'margin-top: 20px', 'required':'False'}),
                    'fname': forms.TextInput(attrs={'required':'False', 'placeholder':'Vorname'}),
                    'lname': forms.TextInput(attrs={'required':'False', 'placeholder':'Nachname'}),
                    'tel': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':'Mobil-Nummer'}),
                    'email': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':'Email Adresse'}),
                    'beschreibung': forms.Textarea(attrs={'style':'height:150px; margin-top:20px;', 'required':'False', 'placeholder':'zustzliche Angaben'}),
                }

class ArchitektFormular(forms.ModelForm):
    class Meta:
        model = ArchitektForm
        fields = {'neubauprojekt','aufstockung','innenumbau','sanierung','weitere','auftragsbeschreibung','fname','lname', 'firm_name','mailList','datum','tel','email','beschreibung'}
        labels = {
                    'neubauprojekt':'',
                    'aufstockung':'',
                    'innenumbau':'',
                    'sanierung':'',
                    'weitere':'',
                    'auftragsbeschreibung':'',
                    'fname':'',
                    'lname':'',
                    'firm_name':'',
                    'mailList':'',
                    'datum':'',
                    'tel':'',
                    'email':'',
                    'beschreibung':'',
                }
        widgets = {
                    'neubauprojekt': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'aufstockung': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'innenumbau': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'sanierung': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'weitere': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'auftragsbeschreibung': forms.Textarea(attrs={'style':'height:150px; margin-top:20px;', 'required':'False', 'placeholder':'Bschreiben Sie Ihren Auftrag.'}),
                    'mailList': forms.Textarea(attrs={'id':'mailList', 'style':'height:150px; margin-top:20px; display:none;', 'required':'False'}),
                    'firm_name': forms.Textarea(attrs={'id':'id_send', 'style': 'height:150px; margin-top:20px', 'placeholder': 'Anfragen werden an Unternehmen in der Liste weitergeleitet.', 'required':'False', 'readonly':'True'}),
                    'datum': forms.TextInput(attrs={'type':'date', 'id':'date' , 'style':'margin-top: 20px', 'required':'False'}),
                    'fname': forms.TextInput(attrs={'required':'False', 'placeholder':'Vorname'}),
                    'lname': forms.TextInput(attrs={'required':'False', 'placeholder':'Nachname'}),
                    'tel': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':'Mobil-Nummer'}),
                    'email': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':'Email Adresse'}),
                    'beschreibung': forms.Textarea(attrs={'style':'height:150px; margin-top:20px;', 'required':'False', 'placeholder':'zustzliche Angaben'}),
                }

class SanitaerFormular(forms.ModelForm):
    class Meta:
        model = SanitaerForm
        fields = {'anlagen','heizung','reparaturen','amaturen','allgemein','auftragsbeschreibung','fname','lname', 'firm_name','mailList','datum','tel','email','beschreibung'}
        labels = {
                    'anlagen':'',
                    'heizung':'',
                    'reparaturen':'',
                    'amaturen':'',
                    'allgemein':'',
                    'auftragsbeschreibung':'',
                    'fname':'',
                    'lname':'',
                    'firm_name':'',
                    'mailList':'',
                    'datum':'',
                    'tel':'',
                    'email':'',
                    'beschreibung':'',
                }
        widgets = {
                    'anlagen': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'heizung': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'reparaturen': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'amaturen': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'allgemein': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'auftragsbeschreibung': forms.Textarea(attrs={'style':'height:150px; margin-top:20px;', 'required':'False', 'placeholder':'Bschreiben Sie Ihren Auftrag.'}),
                    'mailList': forms.Textarea(attrs={'id':'mailList', 'style':'height:150px; margin-top:20px; display:none;', 'required':'False'}),
                    'firm_name': forms.Textarea(attrs={'id':'id_send', 'style': 'height:150px; margin-top:20px', 'placeholder': 'Anfragen werden an Unternehmen in der Liste weitergeleitet.', 'required':'False', 'readonly':'True'}),
                    'datum': forms.TextInput(attrs={'type':'date', 'id':'date' , 'style':'margin-top: 20px', 'required':'False'}),
                    'fname': forms.TextInput(attrs={'required':'False', 'placeholder':'Vorname'}),
                    'lname': forms.TextInput(attrs={'required':'False', 'placeholder':'Nachname'}),
                    'tel': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':'Mobil-Nummer'}),
                    'email': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':'Email Adresse'}),
                    'beschreibung': forms.Textarea(attrs={'style':'height:150px; margin-top:20px;', 'required':'False', 'placeholder':'zustzliche Angaben'}),
                }

class BodenbelaegeFormular(forms.ModelForm):
    class Meta:
        model = BodenbelaegeForm
        fields = {'groesse','parkett','laminat','teppich','vinyl','weitere','auftragsbeschreibung','fname','lname', 'firm_name','mailList','datum','tel','email','beschreibung'}
        labels = {
                    'groesse':'',
                    'parkett':'',
                    'laminat':'',
                    'teppich':'',
                    'vinyl':'',
                    'weitere':'',
                    'auftragsbeschreibung':'',
                    'fname':'',
                    'lname':'',
                    'firm_name':'',
                    'mailList':'',
                    'datum':'',
                    'tel':'',
                    'email':'',
                    'beschreibung':'',
                }
        widgets = {
                    'groesse': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'parkett': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'laminat': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'teppich': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'vinyl': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'weitere': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':''}),
                    'auftragsbeschreibung': forms.Textarea(attrs={'style':'height:150px; margin-top:20px;', 'required':'False', 'placeholder':'Bschreiben Sie Ihren Auftrag.'}),
                    'mailList': forms.Textarea(attrs={'id':'mailList', 'style':'height:150px; margin-top:20px; display:none;', 'required':'False'}),
                    'firm_name': forms.Textarea(attrs={'id':'id_send', 'style': 'height:150px; margin-top:20px', 'placeholder': 'Anfragen werden an Unternehmen in der Liste weitergeleitet.', 'required':'False', 'readonly':'True'}),
                    'datum': forms.TextInput(attrs={'type':'date', 'id':'date' , 'style':'margin-top: 20px', 'required':'False'}),
                    'fname': forms.TextInput(attrs={'required':'False', 'placeholder':'Vorname'}),
                    'lname': forms.TextInput(attrs={'required':'False', 'placeholder':'Nachname'}),
                    'tel': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':'Mobil-Nummer'}),
                    'email': forms.TextInput(attrs={'style':'background-color:transparent', 'required':'False', 'placeholder':'Email Adresse'}),
                    'beschreibung': forms.Textarea(attrs={'style':'height:150px; margin-top:20px;', 'required':'False', 'placeholder':'zustzliche Angaben'}),
                }
