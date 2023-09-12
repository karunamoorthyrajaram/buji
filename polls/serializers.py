from rest_framework import serializers
from polls.models import Student

class StudentSerializers(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            'name': instance.name,
            'age': instance.age
        }
