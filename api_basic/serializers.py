from django.db import models
from django.db.models import fields
from rest_framework import serializers
from api_basic. models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id','title','author']

