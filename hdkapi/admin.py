from django.contrib import admin

#import Api models
from .models import AppUser,Category,Diary,TPWords


# Register Api Models
# Models AppUser,Category,Diary,TPWords

admin.site.register(AppUser)
admin.site.register(Category)
admin.site.register(Diary)
admin.site.register(TPWords)