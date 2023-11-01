# chatbot_app/models.py
from django.db import models

class TrainData(models.Model):
    question = models.TextField()
    intent = models.CharField(max_length=255)

class KnowledgeBase(models.Model):
    intent = models.CharField(max_length=255)
    response = models.TextField()
