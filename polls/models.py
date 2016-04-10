from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class Question(models.Model):

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']

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

    @python_2_unicode_compatible
    def __str__(self):
        return self.choice_text
