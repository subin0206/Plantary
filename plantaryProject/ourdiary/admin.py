from django.contrib import admin
from .models import Ourdiary
from .models import Like
from .models import Comment
# Register your models here.

admin.site.register(Ourdiary)
admin.site.register(Like)
admin.site.register(Comment)