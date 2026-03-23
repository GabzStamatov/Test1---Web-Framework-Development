from django.contrib import admin
from .models import *

admin.site.register(Salesperson)
admin.site.register(Customer)
admin.site.register(Mechanic)
admin.site.register(Car)
admin.site.register(SalesInvoice)
admin.site.register(ServiceTicket)
admin.site.register(Service)
admin.site.register(Parts)
admin.site.register(ServiceMechanic)
admin.site.register(PartsUsed)