# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    
   
    list_display = ['email', 'username', 'role', 'date_of_birth']
    
   
    fieldsets = UserAdmin.fieldsets + (
        ('Role', {'fields': ('role',)}),
    )
    

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Role', {'fields': ('role',)}),
    )

  
    search_fields = ('username', 'email',)
    

    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)
