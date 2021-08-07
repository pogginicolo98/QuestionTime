from django.db import models
from django.conf import settings


class Question(models.Model):
    """
    Questions are written by users and they can have multiple answers.
    Each question is identified by the 'slug' field.
    """

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='questions')
    content = models.CharField(max_length=240)
    slug = models.SlugField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content


class Answer(models.Model):
    """
    Answers belong to a question.
    Each user can write only one answer for each question.
    Any user can vote on any answer.
    """

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    body = models.TextField()
    voters = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='votes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author.username
