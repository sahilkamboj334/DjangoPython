from rest_framework import serializers
from .models import IssueModel

class IssueModelSerializer(serializers.ModelSerializer):

    class Meta:
        model=IssueModel
        fields='__all__'