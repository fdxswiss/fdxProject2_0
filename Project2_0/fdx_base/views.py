# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from fdx_mail.forms import *
from fdx_mail.form_req import SendMassMail
from .firm import Firmeneintrag_new
from .search_plz import Search
from fdx_google.geocoords import geo
from .models import Firma
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random
from django.contrib import messages
from HT import GOOGLE_KEY
from django.core.mail import send_mail

firm_list = Firma.objects.all()

def index(request):

    context = {}

    return render(request, 'index.html', context)

def show(request, name):

    global firm_list

    n = name
    q = request.POST.get("query")

    firma = Firmeneintrag_new()
    f = firma.loadF(name)
    f_mix = list(f)
    random.shuffle(f_mix)

    geocode = geo.getAllGeocoords(f)
    lat, lng, firm_id = geocode

    forms = {
        'Umzug': UmzugFormular(),
        'Reinigung': ReinigungFormular(),
        'Maler': MalerFormular(),
        'Schreiner': SchreinerFormular(),
        'Sanitaer': SanitaerFormular(),
        'Dachdecker': DachdeckerFormular(),
        'Gartenbau': GartenbauFormular(),
        'Architekt': ArchitektFormular(),
        'Elektriker': ElektrikerFormular(),
        'Bodenbelaege': BodenbelaegeFormular(),
    }

    form = forms.get(n)

    firm_name = []
    for f_search in f:
        for id in firm_id:
            if f_search.id == id:
                firm_name.append(f_search)

    # Suche nach Postleitzahl
    if q and q.isnumeric() and len(q) == 4:
        search = Search()
        # lat, lng, firm_id = geocode[n]
        # print(firm_id)
        firm_search, dist = search.filter_plz(f, q)
        firm_search_name = firm_search

        firm_name = []
        for f_search in f:
            for id in firm_id:
                if f_search.id == id:
                    firm_name.append(f_search)

        #GET DISTANCE WITH MATH
        # dist_math = geo.get_distance(q, geocode[n], firm_search)
        # dist_math.sort()
        # print("DIST_MATH : ", dist_math)

        # PAGINATOR
        # firm_search = pagi(request, firm_search, 30)

        context = {
            's_id': request.session.session_key,
            'title': n,
            'firma_new': firm_search,
            'query': q,
            'form': form,
            'lat': lat,
            'lng': lng,
            'distance': dist,
            'anz': len(firm_search),
            'anz_f': firm_list.count(),
            # 'anz_a': a.count()*3,
            'firm_id': firm_id,
            'firm_name': firm_name,
            'GOOGLE_KEY': GOOGLE_KEY
        }

        return render(request, 'branchen/show.html', context)
    elif q and len(q) < 4:
        messages.warning(request, 'Schweizer Postleitzahl eintragen. Beispiel: "8000" für Zürich')
    elif q and q.isnumeric() == False:
        messages.warning(request, 'Schweizer Postleitzahl eintragen. Beispiel: "8000" für Zürich')

    # PAGINATOR
    f_mix = pagi(request, f_mix, 5)

    context = {
        's_id': request.session.session_key,
        'title': n,
        'firma_new': f_mix,
        'form': form,
        'lat': lat,
        'lng': lng,
        'anz': f.count(),
        'anz_f': firm_list.count(),
        # 'anz_a': a.count()*3,
        'firm_name': firm_name,
        'firm_id': firm_id,
        'GOOGLE_KEY': GOOGLE_KEY
    }

    return render(request, 'branchen/show.html', context)



######## OFFERTEN ANFRAGE FORMULAR ########
def formcheck(request):

    context = {
        'form': request.POST,
    }

    return render(request, 'responses/offerResponseSite.html', context)

def formsend(request):
    #
    # # sendTo = SendMassMail()
    # # mail_list = sendTo.sendmailtofirms(request)
    # #
    # print("TITLE: ___________________________________", request.POST.get("title"))
    #
    # forms = {
    #     'Umzug': UmzugFormular(request.POST),
    #     'Reinigung': ReinigungFormular(request.POST),
    #     'Maler': MalerFormular(request.POST),
    #     'Schreiner': SchreinerFormular(request.POST),
    #     'Sanitaer': SanitaerFormular(request.POST),
    #     'Dachdecker': DachdeckerFormular(request.POST),
    #     'Gartenbau': GartenbauFormular(request.POST),
    #     'Architekt': ArchitektFormular(request.POST),
    #     'Elektriker': ElektrikerFormular(request.POST),
    #     'Bodenbelaege': BodenbelaegeFormular(request.POST),
    # }
    #
    # if request.POST:
    #     form = forms.get(request.POST.get("title"))
    #     form.save(commit=True)
    #     print("save = True")

    context = {
        # 'form': form,
    }

    return render(request, 'responses/offertenanfrage.html', context)

######### PAGINATOR ##########

def pagi(request, f, anz):

    page = request.GET.get('page', 1)
    paginator = Paginator(f, anz)

    try:
        f = paginator.page(page)
    except PageNotAnInteger:
        f = paginator.page(1)
    except EmptyPage:
        f = paginator.page(paginator.num_pages)

    return f

############# FIRMFORM ###########
def firmaForm(request):
    # form = EintragFormular()
    # if request.POST:
    #     form = EintragFormular(request.POST)
    #     if form.is_valid():
    #         form.save(commit=True)
    #
    #         subject = "Firmeneintrag -- " + request.POST.get("firma")
    #         message = "Name:" + request.POST.get("name") + "------ Email:" + request.POST.get("eMail") + "------ Ort: " + request.POST.get("plz") + " " + request.POST.get("ort")
    #         send_from = 'info@firmdx.ch'
    #         mail_to = 'admin@firmdx.ch'
    #
    #         send_mail(subject, message, send_from, [mail_to])
    #
    #         return render(request, 'nav/firmaForm.html', { 'send_new_firm' : True,})

    context = {
        # 'form': form,
    }

    return render(request, 'nav/firmaForm.html', context)

############## INFOSITES ################

def impressum(request):

    context = {
        'title': 'Impressum',
    }

    return render(request, 'nav/impressum.html', context)


def aboutUs(request):
    context = {
        'title': 'About us',
    }

    return render(request, 'nav/aboutUs.html', context)


def agb(request):
    context = {
        'title': 'AGB',
    }

    return render(request, 'nav/agb.html', context)

def form_req(request):
    if request.POST.get("fname"):
        print("Formular Name:")
    return

def kontakt(request):
    # form = Kontaktformular()
    # if request.POST:
    #     form = Kontaktformular(request.POST)
    #     if form.is_valid():
    #         form.save(commit=True)
    #
    #         subject = "Kontakt Formular -- " + request.POST.get("eMail")
    #         message = request.POST.get("beschreibung") + " ---------- Tel:" + request.POST.get("tel") + " ---------- Email: " + request.POST.get("eMail") + " ---------- Name: " + request.POST.get("name")
    #         send_from = 'info@firmdx.ch'
    #         mail_to = 'admin@firmdx.ch'
    #
    #         send_mail(subject, message, send_from, [mail_to])
    #
    #         context = {
    #             'title': 'Kontakt',
    #             'send': True,
    #         }
    #
    #         return render(request, 'nav/kontakt.html', context)
    #
    context = {
        # 'title': 'Kontakt',
        # 'form': form,
    }

    return render(request, 'nav/kontakt.html', context)
