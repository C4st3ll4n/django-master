from rest_framework import serializers

from .models import Reaction


class ReactionSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()

    def get_created_at(self, obj):
        now = obj.created_at
        formatted_date = now.strftime("%d/%m/%Y %H:%M:%S")
        return formatted_date

    def get_updated_at(self, obj):
        then = obj.updated_at
        formatted_date = then.strftime("%d/%m/%Y %H:%M:%S")
        return formatted_date

    class Meta:
        model = Reaction
        exclude = ["pkid", "updated_at", "created_at"]
