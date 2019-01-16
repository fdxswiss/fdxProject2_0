# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Firmeneintrag ,Kontaktanfrage, SanitaerForm, UmzugForm, ReinigungForm, MalerForm, DachdeckerForm, ElektrikerForm, ArchitektForm, GartenbauForm, SchreinerForm, BodenbelaegeForm

admin.site.register(Firmeneintrag)
admin.site.register(Kontaktanfrage)
admin.site.register(UmzugForm)
admin.site.register(ReinigungForm)
admin.site.register(MalerForm)
admin.site.register(DachdeckerForm)
admin.site.register(ElektrikerForm)
admin.site.register(ArchitektForm)
admin.site.register(GartenbauForm)
admin.site.register(SchreinerForm)
admin.site.register(SanitaerForm)
admin.site.register(BodenbelaegeForm)
