from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'gender_probability', 'gender_size', 'age', 'age_group', 'country', 'country_probability', 'created_at')
    search_fields = ('name', 'gender', 'age_group', 'country')
# Register your models here.
