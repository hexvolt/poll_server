from rest_framework.viewsets import ModelViewSet

from polls.models import Question, Choice
from polls.serializers import QuestionSerializer


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
