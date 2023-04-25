from rest_framework import serializers

from .models import Person, ImageURL


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageURL
        fields = ["url"]


class ImagesField(serializers.RelatedField):

    def to_internal_value(self, data):
        return data

    def to_representation(self, value):
        return value.url


class PersonSerializer(serializers.ModelSerializer):
    create_date = serializers.DateTimeField(read_only=True)
    update_date = serializers.DateTimeField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    images = ImagesField(read_only=True, many=True)

    class Meta:
        model = Person
        fields = [
            "id",
            "create_date",
            "update_date",
            "person_name",
            "person_birth_date",
            "person_arrest_date",
            "person_death_date",
            "mem_book_note",
            "images"
        ]

