from django.contrib import admin
# Register your models here.
from .models import Team, Player, User, Trade, Stat

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(User)
admin.site.register(Trade)
admin.site.register(Stat)