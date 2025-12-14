from rest_framework import serializers
from .models import Main_Content


class MainContentSerializer(serializers.ModelSerializer):
    # 自动处理缺失协议的 URL
    B_A_S = serializers.SerializerMethodField()

    class Meta:
        model = Main_Content
        fields = '__all__'

    def get_B_A_S(self, obj):
        url = obj.B_A_S or ''
        if url and not url.startswith('http'):
            url = 'https://' + url
        return url