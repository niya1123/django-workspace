"""model"""
import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    """Questionクラス"""
    question_text = models.CharField('質問',max_length=200)
    pub_date = models.DateTimeField('日付')

    def was_published_recently(self):
        """投稿日時の表示"""
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        """ 文字に変換"""
        return self.question_text

class Choice(models.Model):
    """Choiceクラス"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """文字に変換"""
        return self.choice_text