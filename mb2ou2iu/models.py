from django.db import models

class Main_Content(models.Model):
    B_I = models.IntegerField("字段号", primary_key=True)  # 如果 B_I 是唯一字段可加 primary_key=True
    B_H = models.CharField("标题", max_length=32, null=True, blank=True)
    B_A_S = models.CharField("地址", max_length=255, null=True, blank=True)
    B_L = models.CharField("LOGO", max_length=255, null=True, blank=True)

    class Meta:
        managed = False 
        db_table = "main_content"
        verbose_name = "内容"
        verbose_name_plural = "内容"

