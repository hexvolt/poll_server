from rest_framework import status
from rest_framework.decorators import detail_route
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from polls.models import Question, Choice
from polls.serializers import QuestionSerializer, ChoiceSerializer, \
    VoteSerializer


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (AllowAny,)

    @detail_route(methods=['post'])
    def vote(self, request,  pk=None):
        question = self.get_object()

        serializer = VoteSerializer(question=question, data=request.data)

        if serializer.is_valid():
            serializer.validated_data['choice'].vote()
            return Response({'result': 'vote accepted'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class ChoiceViewSet(ModelViewSet):
    queryset = Choice.objects.all().order_by('-question')
    serializer_class = ChoiceSerializer
    permission_classes = (AllowAny,)
