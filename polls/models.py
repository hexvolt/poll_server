from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class Question(models.Model):

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']

    @property
    def serialized_data(self):
        from polls.serializers import QuestionSerializer

        return QuestionSerializer(self).data

    @python_2_unicode_compatible
    def __str__(self):
        return self.question_text


class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                 related_name='choices')

    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def vote(self):
        self.votes += 1
        self.save()

    @property
    def serialized_data(self):
        from polls.serializers import ChoiceSerializer

        return ChoiceSerializer(self).data

    @python_2_unicode_compatible
    def __str__(self):
        return self.choice_text
