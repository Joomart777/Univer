from rest_framework import serializers

from univer_app.models import Univer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Univer

        fields = '__all__'