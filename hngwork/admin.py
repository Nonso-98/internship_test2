from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'name', 'gender', 'gender_probability', 'sample_size', 'age', 'age_group', 'country_id', 'country_probability', 'created_at')
    search_fields = ('name', 'gender', 'age_group', 'country_id')
# Register your models here.
