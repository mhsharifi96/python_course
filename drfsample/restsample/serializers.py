from rest_framework import serializers

from ajaxsample.models import Poll,Choice,Vote

class VoteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Vote
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = '__all__'

class PollSerializers(serializers.ModelSerializer):


    class Meta :
        model = Poll
        fields = '__all__'