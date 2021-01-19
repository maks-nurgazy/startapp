from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    owner_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'id',
            "company_name",
            "username",
            "password",
            "owner_name",
            "first_name",
            "last_name",
            "phone",
            "address",
        )
        read_only_fields = ('owner_name',)
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'write_only': True},
            'last_name': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        text = validated_data.get('first_name', instance.first_name)
        print(text)
        return instance

    def get_owner_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'
