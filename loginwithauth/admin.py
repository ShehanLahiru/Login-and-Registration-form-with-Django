from django.contrib import admin
from django.utils import timezone
from .models import user,review,complaint

class UserAdmin(admin.ModelAdmin):
    change_list_template = 'admin/base_site.html'

"""
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','nic','email','nickname','date_created','last_modified')
    search_fields = ['nickname']
    #list_per_page
    actions = ('change_email',)

    def change_email(self,request,queryset):
        count = queryset.update(email = 'qwerty@gmail.com') 
        self.message_user(request,'{} emails has updated.'.format(count))
    change_email.short_description = 'Change the email'

    

admin.site.register(user,UserAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id','user_id','queAndAnsr','geo_tag','device_signature','date_created','last_modified','days_since_creation')
    date_hierarchy = 'date_created'

    def days_since_creation(self,review):
        diff = timezone.now() - review.date_created
        return diff.days
    days_since_creation.short_description = 'Days Active'
admin.site.register(review,ReviewAdmin)



class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('id','user_id','geo_tag','description','date_created','last_modified','days_since_creation')
    date_hierarchy = 'date_created'

    def days_since_creation(self,complaint):
        diff = timezone.now() - complaint.date_created
        return diff.days
    days_since_creation.short_description = 'Days Active'
admin.site.register(complaint,ComplaintAdmin)
"""
