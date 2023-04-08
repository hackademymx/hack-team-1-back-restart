from rest_framework import serializers
from .models import Comment

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'place',
            'comment',
            'created',
        )

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'place': {
                'id': instance.place.id,
                'name': instance.place.name
            },
            'comment': instance.comment,
            'created': instance.created
        }