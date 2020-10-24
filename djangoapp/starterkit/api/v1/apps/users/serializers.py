from .models import User
from rest_framework import serializers



class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'name')
        extra_kwargs = {'password': {'write_only': True}, }

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.save()
        # AuthToken.objects.create(user)
        return user


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 'email',  'name', 'second_name', 'average_check','frequently_visited_places', 'favorite_places')

