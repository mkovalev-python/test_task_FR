"""
Author: mkovalev
Date: 13/04/2021 11:17

"""
from datetime import datetime

from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from API_v0.models import Polls, Questions, Choices
from API_v0.serializers import PollSerializer, QuestionSerializer


class PollApi(APIView):
    permission_classes = (permissions.IsAdminUser,)

    @staticmethod
    def post(request):
        serializer = PollSerializer(data={'name_poll': request.data['name_poll'],
                                          'date_start': datetime.now(),
                                          'date_finish': request.data['date_finish'],
                                          'description': request.data['description']})
        if serializer.is_valid():
            serializer.save()

            create_questions = request.post('/question/post/',data={'poll_id':serializer.data.id,
                                                                    'questions': request.data.questions})

            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def put(request, pk):
        serializer = PollSerializer(instance=Polls.objects.get(pk=pk),
                                    data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(pk):
        delete_questions = Questions.objects.filter(poll_id=pk)
        for el in delete_questions:
            el.delete()
        Polls.objects.get(pk=pk).delete()

        return Response(status.HTTP_200_OK)


class QuestionApi(APIView):
    permission_classes = (permissions.IsAdminUser,)

    @staticmethod
    def post(request):
        for el in request.data.questions:
            serializer = QuestionSerializer(poll_id=request.data['poll_id'],
                                            question=el['question'],
                                            type=el['type']).save()
            if el['type'] == 'choice' or 'multichoice':
                for d in el['question'].choices:
                    Choices(question_id=serializer.data.id,choice=d).save()

    @staticmethod
    def put(request, pk):
        serializer = QuestionSerializer(instance=Questions.objects.get(pk=pk),
                                    data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(pk):
        question = Questions.objects.get(pk=pk)
        if question.type == 'text':
            question.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            for el in Choices.objects.filter(questions_id=pk):
                el.delete()
            question.delete()
            return Response(status=status.HTTP_200_OK)

