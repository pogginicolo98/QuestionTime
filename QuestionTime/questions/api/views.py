from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from questions.api.permissions import IsAuthorOrReadOnly
from questions.api.serializers import AnswerSerializer, QuestionSerializer
from questions.models import Answer, Question


class QuestionViewSet(viewsets.ModelViewSet):
    """
    CRUD ViewSet:
    - Create a new Question instance.
    - Retrieve a list of all Question instances or a specific one.
    - Update a specific Question instance.
    - Delete a specific Question instance.

    * Only authenticated users can perform any action.
    * Users can update/delete only their own Questions.
    """

    queryset = Question.objects.all().order_by('-updated_at')
    lookup_field = "slug"
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AnswerCreateAPIView(generics.CreateAPIView):
    """
    An APIView that provides 'create()' action.
    Create a new Answer instance.

    * Only authenticated users can perform any action.
    """

    queryset = Answer.objects.all().order_by('created_at')
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Override 'perform_create()' method of CreateModelMixin class.
        Prevents users who have already Answered a specific Question from Answering a second time.

        * Method called when creating a new instance after receiving a POST request.
        """

        request_user = self.request.user
        kwarg_slug = self.kwargs.get('slug')
        question = get_object_or_404(Question, slug=kwarg_slug)

        if question.answers.filter(author=request_user).exists():
            raise ValidationError('You have already answered this question!')
        serializer.save(author=request_user, question=question)


class QuestionAnswerListAPIView(generics.ListAPIView):
    """
    An APIView that provides 'list()' action.
    Retrieve a list of all Answers related to a specific Question.

    * Only authenticated users can perform any action.
    """

    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get('slug')
        return Answer.objects.filter(question__slug=kwarg_slug).order_by('created_at')


class AnswerRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    An APIView that provides 'retrieve()', 'update()', 'delete()' actions.
    - Retrieve a specific Answer.
    - Update a specific Answer.
    - Delete a specific Answer.

    * Only authenticated users can perform any action.
    * Users can update/delete only their own Answers.
    """

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
