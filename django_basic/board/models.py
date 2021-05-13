from django.db import models
class Board(models.Model):
    title = models.CharField(verbose_name='제목', max_length=128)
    contents = models.TextField(verbose_name='내용')                   
    writer = models.ForeignKey('user.User', verbose_name='작성자', on_delete=models.CASCADE)   
    tags = models.ManyToManyField('tag.Tag', verbose_name='태그')           
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return self.title  
    class Meta:
        db_table = 'board'
        verbose_name = '게시글'
        verbose_name_plural = '게시글'     

    # board - tag 사이에 board-tag 테이블이 하나 생겨서 1:n board-tag n: 1  이런식으로 된다 board tag에는 board와 tag의 주키들이 묶여서 주키가됨.
    