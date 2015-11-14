from django.contrib import admin
from .models import User, Dispute

#admins
class UserAdmin(admin.ModelAdmin):
	fieldsets = [(None, {'fields': ['username']}), 
	('Personal Information', {'fields': ['first_name', 'last_name', 'address', 'email'], 'classes':['collapse']})
	]

# Register your models here.
admin.site.register(User, UserAdmin)



admin.site.register(Dispute)
