import datetime
import pytz
# from .forms import Anfrage
from fdx_base.models import Firma
from django.template import loader
# from .models import OffertenAnfrage
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render_to_response
# from servicePrMail.models import TempEMail

# class SendMailToHost:
#
#     def __init__(self):
#         self.data = []
#
#     def sendMail(self, request, form):
#
#         form = self.form
#         if form.is_valid():


class FormCatcher:

    def __init__(self):
        self.data = []

    def catch(self):

        if request.Post:
            print(request.Post)

class SendMassMail:

    def __init__(self):
        self.data = []

    def sendmailtofirms(self, request):

        form = Anfrage(request.POST)
        f = []

        if form.is_valid():

            now = datetime.datetime.now()
            tz = datetime.timedelta(minutes=10)

            utc = pytz.UTC
            temps = TempEMail.objects.all()

            for temp in temps:

                time = temp.updated.replace(tzinfo=utc)
                now = now.replace(tzinfo=utc)

                if time < (now - tz):
                    TempEMail.objects.filter(updated=temp.updated).delete()

            cmail = request.POST.get("eMail")
            t = TempEMail.objects.filter(tempMail=cmail)

            if t:
                return 0
            else:
                form.save(commit=True)

            Anfrage_id = OffertenAnfrage.objects.latest('id')

            TempEMail.objects.create(tempMail=cmail)

            mail_list = request.POST.get("mailList")
            mailList = mail_list.split(", ")
            mailList.append("admin@firmdx.ch")

            text1 = str(mailList[0])
            f += Firma.objects.filter(eMail=text1[1:])

            subject = 'Firmdx - Offertenanfrage - ' + str(Anfrage_id)
            message = request.POST.get("beschreibung")
            send_from = 'info@firmdx.com'
            EMAIL_CUSTOM = request.POST.get("email")

            html_message = loader.render_to_string('responses/offertenanfrage.html',
                {
                    'message': message,
                    'email': request.POST.get("email"),
                    'name': request.POST.get("fname"),
                    'tel': request.POST.get("tel"),
                    'plz': request.POST.get("von"),
                    'ort': request.POST.get("ort"),
                }
            )

            m = 0
            while m < len(mailList):
                send_mail(subject, message, send_from, [mailList[m]], html_message=html_message)
                f += Firma.objects.filter(eMail=mailList[m])
                m += 1


            html_message_custom = loader.render_to_string('responses/offertenanfrage_kunde.html',
                {
                    'message': message,
                    'email': request.POST.get("eMail"),
                    'name': request.POST.get("name"),
                    'tel': request.POST.get("tel"),
                    'plz': request.POST.get("plz"),
                    'ort': request.POST.get("ort"),
                    'mail_list' : f,
                }
            )

            send_mail(subject, message, send_from, [EMAIL_CUSTOM], html_message=html_message_custom)

        return f
