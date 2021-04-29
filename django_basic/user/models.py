from django.db import models

class User(models.Model):
    username = models.CharField(verbose_name='사용자명', max_length=64)
    password = models.CharField(verbose_name='비밀번호', max_length=64)
    registered_dttm = models.DateTimeField(verbose_name='등록시간', auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'django_basic_user'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'

