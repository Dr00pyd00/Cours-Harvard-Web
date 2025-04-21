
from django.contrib import admin
from .models import Flight, Airport, Passenger

# Register your models here.


# si je veux que linterface soit personnalisé :
class FlightAdmin(admin.ModelAdmin):
    list_display = ('origin','destination', 'duration', 'id' )

# ET j'ajoute la class au model qui va avec:
admin.site.register(Flight, FlightAdmin)


# la j'ajoute un truc qui fait que je peux directement transeferer les vols :
class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal =('flights',)

admin.site.register(Passenger, PassengerAdmin)







admin.site.register(Airport)

