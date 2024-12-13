# Suggested code may be subject to a license. Learn more: ~LicenseLog:108212178.
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'