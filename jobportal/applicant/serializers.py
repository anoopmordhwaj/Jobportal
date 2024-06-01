from rest_framework import serializers
from .models import Person, Color
from django.contrib.auth.models import User


# this serializer has been build to validated the register data data whether thw email or password are in corerect form or not .

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):

        if data['username']:
            if User.objects.filter(username = data['username']).exists():
                raise serializers.ValidationError('username already taken !')
        
        if data['email']:
            if User.objects.filter(username = data['email']).exists():
                raise serializers.ValidationError('email already taken !')
        
        return data
    
    def create(self, validated_data):
        user = User.objects.create(username = validated_data['username'],email = validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
    
        
        return validated_data

# this serializer has been build to validated the login data whether thw email or password are in corerect form or not .
class loginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.IntegerField()


# i made this color seerializer to get the specific field of the the color model , ----->color_name 
# the main differnece between serializer an ddepth is thst serialzer gives you more control over model data it is
# opun you that waht you wan tto serialize but in case of depth it gives all the data which is needed or not needed

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['color_name']

class PersonSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    color_info = serializers.SerializerMethodField()
    # this is used to add a field into the model without writing it  into the models.py files

    class Meta:
        model = Person
        fields = '__all__'

            # fields = ['name', 'age'] -------------> too serialize specific fields
        # depth = 1
        # this depth allow us to get the all data of the  foreig key model including(id , color etc),but we are intrested in only the color name 
        # exclude = ['name']-----------> this method will exclude serializing name field
    def get_color_info(self, obj):
        color_obj = Color.objects.get(id = obj.color.id)
        return { 'color_name' : color_obj.color_name}


# ths vis known as validation in serializzer it is used to validatee the data thaat is is coming right or not.
    def validate(self, data):
        if data['age'] < 18:
            raise serializers.ValidationError('age should be greater then 18 years')

        special_characters = "!@#$%^&*()-_=+\|[]{;}:/?.>"
        for c in data['name']:
            if c in special_characters:
                raise serializers.ValidationError('name should not contain special characters')
        return data