from pydoc_data.topics import topics
from tabnanny import verbose
from django.db import models

# Create your models here.
class Topic(models.Model):
    """the learning model"""
    #由字符或文本组成的数据，需要存储少量的文本，如名称标题或城市，可使用
    #max_length是最大字符数
    text = models.CharField(max_length=200)
    #DateTimeField记录日期和时间的数据，我们传递了实参auto_now_add=True
    #每当用户创新新主题的时候，这都让Django将这个属性自动设置成当前日期和时间
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """return the model's string expression"""
        return self.text

class Entry(models.Model):
    """learning some specific knowlege about the certain topic"""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        if len(self.text) > 50:
            return self.text[:50] +"..."
        else:
            return self.text