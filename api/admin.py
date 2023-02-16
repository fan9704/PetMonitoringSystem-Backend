from django.contrib import admin

from api.models import Pet, PetType, RecordType, Record, Machine

admin.site.register(Pet)
admin.site.register(PetType)
admin.site.register(RecordType)
admin.site.register(Record)
admin.site.register(Machine)
