from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import UserForm, CreateUserForm
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class AdminUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email",)

class AdminUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
class CustomUserAdmin(UserAdmin):
    # Your other attributes here
    form = AdminUserChangeForm
    add_form = AdminUserCreationForm

    ordering=("email",)
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )

admin.site.register(User, CustomUserAdmin )