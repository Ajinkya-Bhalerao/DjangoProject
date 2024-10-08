from django.contrib import admin
from .models import UserDetails
from .forms import SignUpForm

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password')
    search_fields = ('username', 'email')
    
admin.site.register(UserDetails, UserAdmin)
