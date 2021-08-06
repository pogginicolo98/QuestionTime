from rest_framework import viewsets
from questions.api.permissions import IsAuthorOrReadOnly
from questions.api.serializers import QuestionSerializer
from questions.models import Question


class QuestionViewSet(viewsets.ModelViewSet):
    """
    CRUD ViewSet:
    - Create a new Question instance.
    - Retrieve a list of all Question instances or a specific one.
    - Update a specific Question instance.
    - Delete a specific Question instance.

    * Only authenticated users can retrieve a list of all Question instances or a specific one. (DEFAULT_PERMISSION_CLASSES in settings.py)
    * Users can update/delete only their own Question instances. (permission class IsAuthorOrReadOnly)
    """

    queryset = Question.objects.all().order_by('-updated_at')
    lookup_field = "slug"
    serializer_class = QuestionSerializer
    permission_classes = IsAuthorOrReadOnly

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
