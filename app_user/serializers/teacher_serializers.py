from app_user import serializers
from app_user.models import User


class RegisterSerializer(serializers.ModelSerializer):

    confirm_password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ("id","is_user","is_admin","full_name","phone","password","confirm_password")

    def validate(self, data):
        password = data.get("password")
        confirm_password = data.get("confirm_password")

        if password != confirm_password:
            raise serializers.ValidationError("Passwords must match")

        return data


    def create(self, validated_data):
        password = validated_data.get("password")
        validated_data.pop("confirm_password")

        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.is_active = True
        user.save()
        return user
