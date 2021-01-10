from rest_framework import serializers
from .models import Bucket,Task

class BucketSerializer(serializers.ModelSerializer):
    # tasks = serializers.StringRelatedField(many=True)

    class Meta:
        model = Bucket
        fields =['id','name']


class TaskSerializer(serializers.ModelSerializer):
    # bucket = serializers.StringRelatedField(many=False)

    class Meta:
        model = Task
        fields = ['id','title','completed']