from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
  password = serializers.CharField(
    max_length=68, min_length=6, write_only=True)

  class Meta:
    model = User
    fields = ['email', 'username', 'password', 'telefone', 'cpf',] #can add more fields as we need

  def validate(self, attrs):
    email = attrs.get('email', '')
    username = attrs.get('username', '')

    if not username.isalnum():
      raise serializers.ValidationError('O nome de usuário deve conter apenas caracteres alfanuméricos')
    return attrs

  def create(self, validate_data):
    return User.objects.create_user(**validate_data)