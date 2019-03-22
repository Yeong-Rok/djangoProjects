from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    # def __str__(self) 메소드는 파이썬의 일반적인 메소드인데 (stringize...? 문자열화 함수), print나 str을 쓸 때 object를 string으로 변환해준다. 모든 클래스에 predefined.
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]