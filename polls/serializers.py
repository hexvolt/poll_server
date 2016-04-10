from rest_framework import serializers

from polls.models import Question, Choice


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = ('id', 'question', 'choice_text', 'votes')
        read_only_fields = ('id', 'votes',)


class QuestionSerializer(serializers.ModelSerializer):

    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'question_text', 'pub_date', 'choices')
        read_only_fields = ('id', 'pub_date')


class VoteSerializer(serializers.Serializer):

    choice = serializers.PrimaryKeyRelatedField(queryset=Choice.objects.none())

    def __init__(self, question, *args, **kwargs):
        super(VoteSerializer, self).__init__(*args, **kwargs)

        self.fields['choice'].queryset = question.choices.all()
