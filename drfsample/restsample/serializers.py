from rest_framework import serializers
from django.contrib.auth.models import User #new
from rest_framework.authtoken.models import Token #new

from ajaxsample.models import Poll,Choice,Vote,GroupPoll

class VoteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Vote
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = '__all__'
        # fields = ('choice_text',) # اگر فیلدهای خاصی مد نظر شما بود


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user) 
        return user


class PollSerializers(serializers.ModelSerializer):
    created_by = UserSerializer() #many=True ? error تست کنید 
    choices = ChoiceSerializer(many=True, read_only=True, required=False)
    # https://medium.com/@krishnaregmi/handling-model-relationships-in-django-rest-framework-e0dfbcf1d83e
    # choices = serializers.StringRelatedField(many=True)
    # choices = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # choices = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='polls_detail'
    # )
    class Meta :
        model = Poll
        fields = '__all__'
        # fields = ('question','created_by','choices')
        


class GroupPollSerializers(serializers.ModelSerializer):
    polls = PollSerializers(many=True,read_only=True)
    class Meta:
        model = GroupPoll
        fields = '__all__' 




