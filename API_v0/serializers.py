"""
Author: mkovalev
Date: 13/04/2021 11:19

"""
from rest_framework import serializers

from API_v0.models import Polls, Questions, Choices, Answers


class PollSerializer(serializers.ModelSerializer):
    """JSON сериалайзер модели опросов"""
    questions = serializers.SerializerMethodField()

    class Meta:
        model = Polls
        field = '__all__'

    def get_questions(self):
        question = Questions.objects.get(poll_id=self.id)
        return QuestionSerializer(question, many=True)

    def create(self, validated_data):
        return Polls.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name_poll = validated_data.get('name_poll', instance.name_poll)
        instance.date_finish = validated_data.get('date_finish', instance.date_finish)
        instance.description = validated_data.get('description', instance.description)

        instance.save()
        return instance


class QuestionSerializer(serializers.ModelSerializer):
    """JSON сериалайзер модели вопросов"""

    choices = serializers.SerializerMethodField()

    class Meta:
        model = Questions
        field = '__all__'

    def get_choices(self):
        choices = Choices.objects.get(question_id=self.id)
        return ChoiceSerializer(choices, many=True)

    def create(self, validated_data):
        return Questions.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.poll_id = validated_data.get('poll_id', instance.poll_id)
        instance.question = validated_data.get('question', instance.question)
        instance.type = validated_data.get('type', instance.type)

        instance.save()
        return instance


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choices
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    poll = serializers.SerializerMethodField

    class Meta:
        model = Answers
        fields = '__all__'

    def get_poll(self):
        poll = Polls.objects.get(id=self.poll_id)
        return PollSerializer(poll, many=True)
