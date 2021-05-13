from django.contrib import admin

# Register your models here.

from test1.models import MatchScore, Table

admin.site.register(MatchScore)
admin.site.register(Table)