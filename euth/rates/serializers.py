from rest_framework import serializers

from .models import Rate


class RateSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = Rate
        read_only_fields = ('modified', 'created', 'id', 'user_name')
        exclude = ('user',)

    def get_user_name(self, obj):
        return str(obj.user.username)
