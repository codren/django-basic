from django.contrib import admin
from .models import Board      

class BoardAdmin(admin.ModelAdmin):
    list_display = ('title',)   # 튜플로 보내줄때 한개 값은 , 꼭 해주기
    
admin.site.register(Board, BoardAdmin)
