from django.contrib import admin

from .models import * 

# admin.site.register(User)

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email','first_name', 'last_name', 'is_staff', 'is_active',)
    list_filter = ('username','email', 'is_staff', 'is_active',)
   
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(UserBase, UserAdmin)
admin.site.register(UserProfile)
admin.site.register(DepositHistory)
admin.site.register(withdrawHistory)
admin.site.register(TransactionHistory)
admin.site.register(Stake)

admin.site.register(ForecasterPrediction)