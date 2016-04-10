from rest_framework import serializers
from rest_framework.serializers import ChoiceField, ModelSerializer, Serializer

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


class VoteSerializer(Serializer):

    choice = serializers.PrimaryKeyRelatedField(queryset=Choice.objects.none())

    def __init__(self, question, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['choice'].queryset = question.choices.all()
