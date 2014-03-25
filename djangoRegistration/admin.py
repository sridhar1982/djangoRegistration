# from django.contrib import admin
# from django.contrib.auth.models import User
# from django.contrib.auth.admin import UserAdmin
# from customRegistration.models import ExUserProfile
# 
# admin.site.unregister(User)
# 
# class UserProfileInline(admin.StackedInline):
#     model = ExUserProfile
# 
# class UserProfileAdmin(UserAdmin):
#     inlines = [ UserProfileInline, ]
#     list_display = ('username', 'email','dateofBirth')
# 
# admin.site.register(User, UserProfileAdmin)
