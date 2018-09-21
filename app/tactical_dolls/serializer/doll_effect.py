from rest_framework import serializers

from ..models import DollEffect

__all__ = (
    'DollEffectSerializer',
)


class DollEffectSerializer(serializers.ModelSerializer):
    effectpos = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = DollEffect
        fields = '__all__'

    def get_effectpos(self, obj):
        return eval(obj.effectpos)
