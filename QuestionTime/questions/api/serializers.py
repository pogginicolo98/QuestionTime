from rest_framework import serializers
from questions.models import Answer, Question


class AnswerSerializer(serializers.ModelSerializer):
    """
    ModelSerializer for Answer instances.

    fields:
    - author
    - body
    - created_at: Date format '1 January 2021'.
    - likes_count: How many users voted this answer.
    - user_has_voted: True, the if user has already voted.
    """

    author = serializers.StringRelatedField(read_only=True)
    likes_count = serializers.SerializerMethodField(read_only=True)
    user_has_voted = serializers.SerializerMethodField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Answer
        exclude = ['question', 'updated_at', 'voters']

    def get_likes_count(self, instance):
        return instance.voters.count()

    def get_user_has_voted(self, instance):
        request = self.context.get("request")
        return instance.voters.filter(pk=request.user.pk).exists()

    def get_created_at(self, instance):
        return instance.created_at.strftime('%d %B %Y')


class QuestionSerializer(serializers.ModelSerializer):
    """
    ModelSerializer for Question instances.

    fields:
    - author
    - content
    - slug
    - created_at: Date format '1 January 2021'.
    - answer_count: How many users answered this question.
    - user_has_answered: True, the if user has already answered.
    """

    author = serializers.StringRelatedField(read_only=True)
    answers_count = serializers.SerializerMethodField(read_only=True)
    user_has_answered = serializers.SerializerMethodField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Question
        exclude = ['updated_at']

    def get_answers_count(self, instance):
        return instance.answers.count()

    def get_user_has_answered(self, instance):
        request = self.context.get('request')
        return instance.answers.filter(author=request.user).exists()

    def get_created_at(self, instance):
        return instance.created_at.strftime('%d %B %Y')
