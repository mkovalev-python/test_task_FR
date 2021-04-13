"""
Author: mkovalev
Date: 12/04/2021 20:37

"""
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from API_v0.models import Polls, Answers
from API_v0.serializers import PollSerializer, AnswerSerializer


class ActivePoll(APIView):

    @staticmethod
    def get(request):
        queryset = Polls.objects.all()
        if permissions.IsAuthenticated:
            for el in Answers.objects.filter(user_id=request.user.id):
                queryset.exlude(id=el.poll_id)

        serializer = PollSerializer(queryset, many=True).data

        return Response(serializer)

    @staticmethod
    def post(request):
        serializer = AnswerSerializer(data={'poll': request.data['poll_id'],
                                            'question': request.data['question_id'],
                                            'answer': request.data['answer'],
                                            'user': request.user.id})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class GetCheckPolls(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    @staticmethod
    def get(request):
        queryset = Answers.objects.filter(user_id=request.user.id)
        serializer = AnswerSerializer(queryset, many=True).data

        return Response(serializer)
