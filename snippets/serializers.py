from django.contrib.auth.models import User
from rest_framework import serializers

from snippets.models import Snippet


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.CharField(read_only=True, source="owner.username")
    highlight = serializers.HyperlinkedIdentityField(
        view_name="snippet-highlight", format="html"
    )

    class Meta:
        model = Snippet
        fields = [
            "url",
            "id",
            "owner",
            "title",
            "code",
            "linenos",
            "language",
            "style",
            "highlight",
        ]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        view_name="snippet-detail", many=True, queryset=Snippet.objects.all()
    )

    class Meta:
        model = User
        fields = ["url", "id", "username", "snippets"]
