from rest_framework import serializers
from djrest.models import Djrest, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class DjrestSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='djrest-highlight', format='html')

    class Meta:
        model = Djrest
        fields = ['url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    djrest = serializers.HyperlinkedRelatedField(many=True, view_name='djrest-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'djrest']

