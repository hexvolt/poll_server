from rest_framework.decorators import detail_route
from rest_framework.viewsets import ModelViewSet

from polls.models import Question, Choice
from polls.serializers import QuestionSerializer, ChoiceSerializer


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    @detail_route(methods=['post'])
    def vote(self, request,  pk=None):
        question = self.get_object()
        pass


class ChoiceViewSet(ModelViewSet):
    queryset = Choice.objects.all().order_by('-question')
    serializer_class = ChoiceSerializer
