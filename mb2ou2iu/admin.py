from django.contrib import admin
from .models import Main_Content

@admin.register(Main_Content)
class MainContentAdmin(admin.ModelAdmin):
    list_display = ("B_I", "B_H", "B_A_S", "B_L")  # 显示字段
    search_fields = ("B_H", "B_A_S", "B_L")        # 支持搜索
    list_editable = ('B_H', 'B_A_S', 'B_L')  # 列表页直接修改
