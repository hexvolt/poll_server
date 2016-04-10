from rest_framework.serializers import ModelSerializer

from polls.models import Question, Choice


class ChoiceSerializer(ModelSerializer):

    class Meta:
        model = Choice
        fields = ('id', 'question', 'choice_text', 'votes')
        read_only_fields = ('id', 'votes',)


class QuestionSerializer(ModelSerializer):

    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'question_text', 'pub_date', 'choices')
        read_only_fields = ('id', 'pub_date')
