from django.contrib import admin
from .models import Poll, Question, Choice, Vote
from .models import Poll, Subscription, User

admin.site.register(Poll)
admin.site.register(Subscription)

class PollAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_active')
    search_fields = ['title']
    list_filter = ('is_active',)
    pass

if not admin.site.is_registered(Poll):
    admin.site.register(Poll, PollAdmin)
