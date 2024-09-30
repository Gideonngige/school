from django.contrib import admin
from . models import Messages, User, Message, Store, Bus, Forest, Coins
# Register your models here.
admin.site.register(Messages)
admin.site.register(User)
admin.site.register(Message)
admin.site.register(Store)
admin.site.register(Forest)
admin.site.register(Bus)
admin.site.register(Coins)

