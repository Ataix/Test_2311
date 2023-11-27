from django.contrib import admin
from django.contrib.auth import get_user_model


BookshelfUser = get_user_model()


@admin.register(BookshelfUser)
class ProfileAdmin(admin.ModelAdmin):
    # readonly_fields = (
    #     'register_date',
    # )

    list_display = (
        'username',
        'email',
        'is_staff',
        'is_superuser',
        'register_date'
    )
    fields = (
        'username',
        'password',
        'email',
        'is_staff',
        'is_superuser',
    )
