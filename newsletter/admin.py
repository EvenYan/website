from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin

# Register your models here.
from .models import SignUp
from .forms import SignUpForm
from .models import Article

class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__str__", "timestamp", "update"]
    form = SignUpForm
    # class Meta:
    #     model = SignUp

admin.site.register(SignUp, SignUpAdmin)
admin.site.register(Article)
