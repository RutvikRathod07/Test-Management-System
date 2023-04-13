from django.db import models


# Create your models here.
class QuesModel(models.Model):
    question = models.CharField(max_length=200, null=True)
    op1 = models.CharField(max_length=200, null=True)
    op2 = models.CharField(max_length=200, null=True)
    op3 = models.CharField(max_length=200, null=True)
    op4 = models.CharField(max_length=200, null=True)


class AnswerModel(models.Model):
    question = models.ForeignKey(QuesModel, on_delete=models.CASCADE)
    ans = models.CharField(max_length=10)
