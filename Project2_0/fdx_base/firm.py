from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Firma

class Firmeneintrag_new:

    def __init__(self):
        self.data = []

    def loadF(self, name):
        self.name = name

        firm_list = Firma.objects.filter(branche__icontains=name)

        return firm_list

    def getFirm(self, name, firm_list):
        self.name = name
        self.firm_list = firm_list

        branchen = {'Umzug': 1, 'Reinigung': 2, 'Maler': 3, 'Bodenbelaege': 11, 'Architekt': 5,
                    'Sanitaer': 6, 'Schreiner': 7, 'Gartenbau': 8, 'Dachdecker': 9, 'Elektriker': 10,}

        branche_auswahl = branchen.get(self.name)
        firm_list = firm_list.filter(branche=branche_auswahl)

        return firm_list
